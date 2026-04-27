from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
ATTEMPTS_DIR = ROOT / "attempts"
REPORTS_DIR = ROOT / "reports"
PROGRESS_DIR = ROOT / "progress"

MANIFEST_PATH = DATA_DIR / "pack-manifest.json"
ATTEMPT_LOG_PATH = DATA_DIR / "attempt-log.json"

VALID_ANSWERS = {"A", "B", "C", "D"}
CONFIDENCE_MAP = {
    "高": "高",
    "中": "中",
    "低": "低",
    "H": "高",
    "M": "中",
    "L": "低",
    "HIGH": "高",
    "MEDIUM": "中",
    "LOW": "低",
}
YES_NO_MAP = {
    "是": "是",
    "否": "否",
    "Y": "是",
    "N": "否",
    "YES": "是",
    "NO": "否",
    "TRUE": "是",
    "FALSE": "否",
    "1": "是",
    "0": "否",
}

ATTEMPT_TEMPLATE_META_RE = re.compile(
    r"<!--\s*attempt-template\s+session-key=(?P<session_key>\S+)\s+session-version=(?P<session_version>\S+)\s*-->"
)


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    ensure_parent(path)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, payload: Any) -> None:
    ensure_parent(path)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8-sig"))


def load_manifest() -> dict[str, Any]:
    manifest = load_json(MANIFEST_PATH, {})
    if not manifest:
        raise FileNotFoundError(f"manifest not found: {MANIFEST_PATH}")
    return manifest


def load_attempt_log() -> dict[str, Any]:
    return load_json(ATTEMPT_LOG_PATH, {"attempts": []})


def save_attempt_log(payload: dict[str, Any]) -> None:
    write_json(ATTEMPT_LOG_PATH, payload)


def parse_attempt_template_meta_text(text: str) -> dict[str, str]:
    match = ATTEMPT_TEMPLATE_META_RE.search(text[:500])
    if not match:
        return {}
    return match.groupdict()


def read_attempt_template_meta(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    return parse_attempt_template_meta_text(path.read_text(encoding="utf-8"))


def session_key(day: int, subject: int) -> str:
    return f"day-{day:02d}-subject-{subject}"


def session_map(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {session["key"]: session for session in manifest.get("sessions", [])}


def session_version_map(manifest: dict[str, Any]) -> dict[str, str]:
    return {session["key"]: session.get("session_version", "") for session in manifest.get("sessions", [])}


def attempt_matches_current_version(attempt: dict[str, Any], versions: dict[str, str] | None) -> bool:
    if not versions:
        return True
    expected = versions.get(attempt["session_key"], "")
    if not expected:
        return True
    return attempt.get("session_version", "") == expected


def latest_attempts_by_key(log: dict[str, Any], versions: dict[str, str] | None = None) -> dict[str, dict[str, Any]]:
    latest: dict[str, dict[str, Any]] = {}
    for attempt in log.get("attempts", []):
        if not attempt_matches_current_version(attempt, versions):
            continue
        key = attempt["session_key"]
        current = latest.get(key)
        if current is None or attempt["submitted_at"] > current["submitted_at"]:
            latest[key] = attempt
    return latest


def best_attempts_by_key(log: dict[str, Any], versions: dict[str, str] | None = None) -> dict[str, dict[str, Any]]:
    best: dict[str, dict[str, Any]] = {}
    for attempt in log.get("attempts", []):
        if not attempt_matches_current_version(attempt, versions):
            continue
        key = attempt["session_key"]
        current = best.get(key)
        if current is None or attempt["score_pct"] > current["score_pct"]:
            best[key] = attempt
    return best


def answer_counts_by_key(log: dict[str, Any], versions: dict[str, str] | None = None) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for attempt in log.get("attempts", []):
        if not attempt_matches_current_version(attempt, versions):
            continue
        counts[attempt["session_key"]] += 1
    return dict(counts)


def normalize_answer(value: str) -> str:
    token = value.strip().upper()
    return token if token in VALID_ANSWERS else ""


def normalize_confidence(value: str) -> str:
    token = value.strip().upper()
    return CONFIDENCE_MAP.get(token, "")


def normalize_yes_no(value: str) -> str:
    token = value.strip().upper()
    return YES_NO_MAP.get(token, "")


def split_answer_blob(blob: str) -> list[str]:
    tokens = re.split(r"[\s,;/|]+", blob.strip())
    return [normalize_answer(token) for token in tokens if token.strip()]


def parse_inline_answer_blob(blob: str) -> tuple[list[str], list[str]]:
    tokens = [token.strip() for token in re.split(r"[\s,;/|]+", blob.strip()) if token.strip()]
    answers: list[str] = []
    invalid: list[str] = []
    for token in tokens:
        normalized = normalize_answer(token)
        if not normalized:
            invalid.append(token)
        answers.append(normalized)
    return answers, invalid


def parse_attempt_markdown(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    meta = parse_attempt_template_meta_text(text)
    rows: list[list[str]] = []
    in_table = False

    for line in text.splitlines():
        if line.startswith("| 題號 |"):
            in_table = True
            continue
        if not in_table:
            continue
        if not line.startswith("|"):
            if rows:
                break
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells or cells[0] in {"---", ":---"}:
            continue
        if cells[0].isdigit():
            rows.append(cells)

    answers: list[str] = []
    confidence: list[str] = []
    explain: list[str] = []
    notes: list[str] = []
    errors: list[str] = []

    for row in rows:
        question_no = row[0] if row else "?"
        raw_answer = row[1].strip() if len(row) > 1 else ""
        raw_confidence = row[2].strip() if len(row) > 2 else ""
        raw_explain = row[3].strip() if len(row) > 3 else ""

        normalized_answer = normalize_answer(raw_answer)
        normalized_confidence = normalize_confidence(raw_confidence)
        normalized_explain = normalize_yes_no(raw_explain)

        if raw_answer and not normalized_answer:
            errors.append(f"題 {question_no} 的答案 `{raw_answer}` 無效，只接受 A/B/C/D。")
        if raw_confidence and not normalized_confidence:
            errors.append(f"題 {question_no} 的把握度 `{raw_confidence}` 無效，只接受 高/中/低。")
        if raw_explain and not normalized_explain:
            errors.append(f"題 {question_no} 的可解釋性 `{raw_explain}` 無效，只接受 是/否。")

        answers.append(normalized_answer)
        confidence.append(normalized_confidence)
        explain.append(normalized_explain)
        notes.append(row[4].strip() if len(row) > 4 else "")

    return {
        "session_key": meta.get("session_key", ""),
        "session_version": meta.get("session_version", ""),
        "answers": answers,
        "confidence": confidence,
        "explain": explain,
        "notes": notes,
        "errors": errors,
    }


def session_title(session: dict[str, Any]) -> str:
    return session.get("display_name") or session["key"]


def session_kind_label(session: dict[str, Any]) -> str:
    return "每日題單" if session.get("kind") == "daily" else "加練題庫"


def session_question_relpath(session: dict[str, Any], prefix: str = "../") -> str:
    return f"{prefix}{session['question_file']}"


def session_attempt_relpath(session: dict[str, Any], prefix: str = "../") -> str:
    return f"{prefix}{session['attempt_file']}"


def session_report_relpath(session: dict[str, Any], prefix: str = "../") -> str:
    return f"{prefix}{session['report_file']}"


def next_review_day(appearance_days: list[int], current_day: int | None) -> int | None:
    if current_day is None:
        return None
    future_days = [day for day in appearance_days if day > current_day]
    return min(future_days) if future_days else None


def next_review_label(
    appearance_days: list[int],
    current_day: int | None,
    fallback: str = "自主加練回鍋",
) -> str:
    review_day = next_review_day(appearance_days, current_day)
    if review_day is None:
        return fallback
    return f"Day {review_day:02d}"


def priority_rank(label: str) -> int:
    return {"A": 0, "B": 1, "C": 2}.get(label, 3)


def render_scoreboard(manifest: dict[str, Any], log: dict[str, Any]) -> str:
    versions = session_version_map(manifest)
    latest_map = latest_attempts_by_key(log, versions)
    best_map = best_attempts_by_key(log, versions)
    count_map = answer_counts_by_key(log, versions)

    def render_rows(sessions: list[dict[str, Any]]) -> list[str]:
        rows: list[str] = []
        for session in sessions:
            key = session["key"]
            latest = latest_map.get(key)
            best = best_map.get(key)
            attempts = count_map.get(key, 0)
            latest_score = "-" if latest is None else f"{latest['score_pct']:.1f}%"
            best_score = "-" if best is None else f"{best['score_pct']:.1f}%"
            last_time = "-" if latest is None else latest["submitted_at"][:16].replace("T", " ")
            status = "未作答"
            if latest is not None:
                status = "已過線" if latest["score_pct"] >= 70 else "需回補"
            rows.append(
                f"| [{session_title(session)}]({session_question_relpath(session)}) | "
                f"{session_kind_label(session)} | {session['subject']} | {session.get('priority', '-')} | {latest_score} | "
                f"{best_score} | {attempts} | {last_time} | {status} |"
            )
        return rows

    daily_sessions = [session for session in manifest.get("sessions", []) if session.get("kind") == "daily"]
    extended_sessions = [session for session in manifest.get("sessions", []) if session.get("kind") == "extended"]

    lines = [
        "# Scoreboard",
        "",
        "顯示每份題單目前最新成績、最佳成績、作答次數與是否過線。",
        "",
        "## 每日題單",
        "",
        "| 題單 | 類型 | 科目 | 優先級 | 最新分數 | 最佳分數 | 作答次數 | 最後作答 | 狀態 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        *(render_rows(daily_sessions) or ["| - | - | - | - | - | - | - | - | - |"]),
        "",
    ]

    if extended_sessions:
        lines.extend(
            [
                "## Extended 加練",
                "",
                "| 題單 | 類型 | 科目 | 優先級 | 最新分數 | 最佳分數 | 作答次數 | 最後作答 | 狀態 |",
                "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
                *(render_rows(extended_sessions) or ["| - | - | - | - | - | - | - | - | - |"]),
                "",
            ]
        )

    return "\n".join(lines)


def aggregate_gap_rows(manifest: dict[str, Any], log: dict[str, Any]) -> list[dict[str, Any]]:
    sessions = session_map(manifest)
    versions = session_version_map(manifest)
    gaps: dict[str, dict[str, Any]] = {}

    for attempt in log.get("attempts", []):
        if not attempt_matches_current_version(attempt, versions):
            continue
        session = sessions.get(attempt["session_key"])
        if session is None:
            continue

        question_map = {question["question_no"]: question for question in session["questions"]}
        current_day = attempt.get("day")

        for result in attempt.get("question_results", []):
            question = question_map.get(result["question_no"])
            if question is None:
                continue

            item_id = question["item_id"]
            row = gaps.setdefault(
                item_id,
                {
                    "item_id": item_id,
                    "subject": session["subject"],
                    "lcode": question["lcode"],
                    "priority": question.get("priority", session.get("priority", "-")),
                    "focus": session["focus"],
                    "source_label": session_title(session),
                    "gaps": question["gaps"],
                    "appearance_days": question.get("appearance_days", []),
                    "wrong_count": 0,
                    "low_confidence_count": 0,
                    "explain_no_count": 0,
                    "last_day": current_day,
                    "last_time": attempt["submitted_at"],
                },
            )

            row["last_day"] = current_day
            row["last_time"] = attempt["submitted_at"]

            if not result["is_correct"]:
                row["wrong_count"] += 1
            if result["confidence"] == "低":
                row["low_confidence_count"] += 1
            if result["can_explain"] == "否":
                row["explain_no_count"] += 1

    rows: list[dict[str, Any]] = []
    for row in gaps.values():
        total_hits = row["wrong_count"] + row["low_confidence_count"] + row["explain_no_count"]
        if total_hits == 0:
            continue
        row["severity"] = "high" if row["wrong_count"] + row["explain_no_count"] >= 2 else "watch"
        row["next_review"] = next_review_label(row["appearance_days"], row["last_day"])
        rows.append(row)

    rows.sort(
        key=lambda row: (
            0 if row["severity"] == "high" else 1,
            priority_rank(row.get("priority", "-")),
            -(row["wrong_count"] + row["low_confidence_count"] + row["explain_no_count"]),
            row["subject"],
            row["lcode"],
            row["item_id"],
        )
    )
    return rows


def render_auto_knowledge_gaps(manifest: dict[str, Any], log: dict[str, Any]) -> str:
    rows = aggregate_gap_rows(manifest, log)
    lines = [
        "# Auto Knowledge Gaps",
        "",
        "根據最新作答紀錄彙整出的弱點。`high` 代表明確錯誤或無法解釋的累積較高，`watch` 代表仍需要回看。",
        "",
        "| 等級 | 科目 | 優先級 | Concept ID | L-code | 錯題次數 | 低把握次數 | 無法解釋次數 | 下次回看 | 來源題單 | 必補知識點 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    if not rows:
        lines.append("| - | - | - | - | - | - | - | - | - | - | 目前沒有自動弱點。 |")
    else:
        for row in rows:
            lines.append(
                f"| {row['severity']} | 科目 {row['subject']} | `{row.get('priority', '-')}` | `{row['item_id']}` | `{row['lcode']}` | "
                f"{row['wrong_count']} | {row['low_confidence_count']} | {row['explain_no_count']} | "
                f"{row['next_review']} | {row['source_label']} | {row['gaps'][0]} |"
            )
    lines.append("")
    return "\n".join(lines)


def render_auto_review_queue(manifest: dict[str, Any], log: dict[str, Any]) -> str:
    rows = aggregate_gap_rows(manifest, log)
    queue: list[tuple[int, dict[str, Any]]] = []
    for row in rows:
        review_day = next_review_day(row["appearance_days"], row["last_day"])
        queue.append((999 if review_day is None else review_day, row))
    queue.sort(key=lambda pair: (priority_rank(pair[1].get("priority", "-")), pair[0], pair[1]["subject"], pair[1]["item_id"]))

    lines = [
        "# Auto Review Queue",
        "",
        "把弱點依照下一次建議回看順序排出來。沒有固定回看日的 extended 題會排在後面，作為手動加練清單。",
        "",
        "| 優先序 | 科目 | 優先級 | Concept ID | L-code | 建議回看 | 來源題單 | 動作 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    if not queue:
        lines.append("| - | - | - | - | - | - | - | 目前沒有回看項目。 |")
    else:
        for index, (_, row) in enumerate(queue, start=1):
            lines.append(
                f"| {index} | 科目 {row['subject']} | `{row.get('priority', '-')}` | `{row['item_id']}` | `{row['lcode']}` | "
                f"{row['next_review']} | {row['source_label']} | 回看 `sources/scope-weight-map.md` 與對應題單解析 |"
            )
    lines.append("")
    return "\n".join(lines)


def render_placeholder_report(session: dict[str, Any]) -> str:
    source_lines = session.get("source_refs") or ["sources/question-source-map.md"]
    return "\n".join(
        [
            "<!-- placeholder-report -->",
            f"# {session_title(session)}｜批改報告",
            "",
            f"- 類型：`{session_kind_label(session)}`",
            f"- 焦點：`{session['focus']}`",
            f"- 優先級：`{session.get('priority', '-')}`",
            f"- 來源層級：`{session.get('source_tier', '-')}`",
            f"- 題庫版本：`{session.get('session_version', '-')}`",
            f"- 題目：[{Path(session['question_file']).name}]({session_question_relpath(session)})",
            f"- 作答單：[{Path(session['attempt_file']).name}]({session_attempt_relpath(session)})",
            f"- 批改指令：`{session['score_command']}`",
            "",
            "## 來源依據",
            "",
            *[f"- {line}" for line in source_lines[:4]],
            "",
            "## 目前狀態",
            "",
            "- 這份報告尚未批改完成。",
            "- 先填作答單，或用 `--answers A,B,C,D,...` 直接批改。",
            "- 批改後會在這裡看到弱點摘要、錯題明細與回看建議。",
            "",
            "## 延伸追蹤",
            "",
            "- 查看整體成績：[scoreboard.md](../progress/scoreboard.md)",
            "- 查看自動弱點：[auto-knowledge-gaps.md](../progress/auto-knowledge-gaps.md)",
            "- 查看回看順序：[auto-review-queue.md](../progress/auto-review-queue.md)",
            "",
        ]
    )


def render_attempt_report(session: dict[str, Any], attempt: dict[str, Any]) -> str:
    question_map = {question["question_no"]: question for question in session["questions"]}
    weak_rows: list[str] = []
    weak_lcodes: dict[str, int] = defaultdict(int)
    current_day = attempt.get("day")
    source_lines = session.get("source_refs") or ["sources/question-source-map.md"]

    for result in attempt["question_results"]:
        is_weak = (
            not result["is_correct"]
            or result["can_explain"] == "否"
            or result["confidence"] == "低"
        )
        if not is_weak:
            continue

        question = question_map[result["question_no"]]
        issue = "答錯"
        if result["is_correct"] and result["can_explain"] == "否":
            issue = "答對但不能解釋"
        elif result["is_correct"] and result["confidence"] == "低":
            issue = "答對但低把握"

        weak_rows.append(
            f"| {result['question_no']} | {result['selected'] or '-'} | {result['correct']} | {issue} | "
            f"`{question['item_id']}` | `{question['lcode']}` | {question['gaps'][0]} | "
            f"{next_review_label(question.get('appearance_days', []), current_day)} |"
        )
        weak_lcodes[question["lcode"]] += 1

    lcode_lines = [
        f"- `{lcode}`：{count} 題需要回看"
        for lcode, count in sorted(weak_lcodes.items(), key=lambda pair: (-pair[1], pair[0]))
    ]
    if not lcode_lines:
        lcode_lines = ["- 本次沒有明顯弱點，維持目前節奏即可。"]

    status = "已過線" if attempt["score_pct"] >= 70 else "未過線，需回補"

    lines = [
        f"# {session_title(session)}｜批改報告",
        "",
        f"- 類型：`{session_kind_label(session)}`",
        f"- 焦點：`{session['focus']}`",
        f"- 優先級：`{session.get('priority', '-')}`",
        f"- 來源層級：`{session.get('source_tier', '-')}`",
        f"- 題庫版本：`{session.get('session_version', '-')}`",
        f"- 成績：`{attempt['correct_count']}/{attempt['total_questions']}` (`{attempt['score_pct']:.1f}%`)",
        f"- 狀態：`{status}`",
        f"- 作答時間：`{attempt['submitted_at'].replace('T', ' ')[:16]}`",
        f"- 題目：[{Path(session['question_file']).name}]({session_question_relpath(session)})",
        f"- 作答單：[{Path(session['attempt_file']).name}]({session_attempt_relpath(session)})",
        "",
        "## 來源依據",
        "",
        *[f"- {line}" for line in source_lines[:4]],
        "",
        "## 弱點摘要",
        "",
        *lcode_lines,
        "",
        "## 需要回看的題目",
        "",
        "| 題號 | 你的答案 | 正解 | 類型 | Concept ID | L-code | 必補知識點 | 下次回看 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    if weak_rows:
        lines.extend(weak_rows)
    else:
        lines.append("| - | - | - | 本次全部穩定 | - | - | 可直接往下一份題單前進 | - |")

    lines.extend(
        [
            "",
            "## 下一步",
            "",
            "- 先回看本報告中的高頻 L-code，再重做同一天或同一組 extended 題。",
            "- 若是 extended 題出錯，建議直接重做同一份 drill，確認不是只記住答案。",
            "",
        ]
    )
    return "\n".join(lines)
