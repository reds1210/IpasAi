from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
from textwrap import dedent

import expanded_question_bank as expanded
import generate_ipas_reverse_pack as pack
import study_pack_lib as lib


ROOT = Path(__file__).resolve().parent


def question_source_refs(item: dict) -> list[str]:
    return list(item.get("source_refs") or item.get("refs", []))


def question_evidence_tags(item: dict) -> list[str]:
    tags = [tag for tag in item.get("evidence_tags", []) if tag]
    if tags:
        return tags

    source_tier = pack.infer_item_source_tier(item)
    if source_tier == "official-derived":
        return ["official-derived", "official-scope"]
    if source_tier == "public-pattern-derived":
        return ["public-pattern-derived", "public-practice"]
    return [source_tier]


def compute_session_version(session_key: str, focus: str, questions: list[dict]) -> str:
    payload = {
        "key": session_key,
        "focus": focus,
        "questions": [
            {
                "question_no": question["question_no"],
                "item_id": question["item_id"],
                "stem_variant": question["stem_variant"],
                "lcode": question["lcode"],
                "stem": question["stem"],
                "options": question["options"],
                "correct": question["correct"],
            }
            for question in questions
        ],
    }
    blob = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    return hashlib.sha1(blob.encode("utf-8")).hexdigest()[:12]


def attempt_sheet_needs_refresh(path: Path, session: dict) -> bool:
    if not path.exists():
        return True
    if attempt_sheet_is_blank(path):
        return True
    meta = lib.read_attempt_template_meta(path)
    return meta.get("session_version") != session.get("session_version")


def backup_stale_attempt(path: Path) -> Path:
    meta = lib.read_attempt_template_meta(path)
    old_version = meta.get("session_version", "legacy")
    stamp = datetime.now().astimezone().strftime("%Y%m%d-%H%M%S")
    backup = path.with_name(f"{path.stem}.stale-{old_version}-{stamp}{path.suffix}")
    lib.write_text(backup, path.read_text(encoding="utf-8"))
    return backup


def build_question_record(
    item: dict,
    q_no: int,
    stem_variant: int,
    subject: int,
    appearance_days: list[int] | None = None,
) -> dict:
    stem = item["stems"][stem_variant]
    options, answer_label = pack.rotate_options(item["correct"], item["distractors"], pack.stable_seed(item["id"] + stem))
    priority = pack.infer_item_priority(item)
    return {
        "question_no": q_no,
        "item_id": item["id"],
        "subject": subject,
        "stem_variant": stem_variant,
        "lcode": item["lcode"],
        "difficulty": item["difficulty"],
        "stem": stem,
        "options": [{"label": label, "text": text} for label, text in options],
        "correct": answer_label,
        "correct_text": item["correct"],
        "gaps": item["gaps"],
        "refs": item["refs"],
        "why_correct": item["why_correct"],
        "priority": priority,
        "priority_reason": pack.infer_item_priority_reason(item),
        "source_tier": pack.infer_item_source_tier(item),
        "source_refs": question_source_refs(item),
        "evidence_tags": question_evidence_tags(item),
        "appearance_days": appearance_days or [],
    }


def build_daily_session(day: int, subject: int) -> dict:
    items = pack.items_for_day(subject, day)
    focus = pack.DAY_META[day]["s1_focus"] if subject == 1 else pack.DAY_META[day]["s2_focus"]
    appearances = pack.S1_APPEARANCES if subject == 1 else pack.S2_APPEARANCES
    priority = pack.infer_session_priority(subject, items)

    questions = []
    q_no = 1
    for item in items:
        appearance_days = appearances.get(item["id"], [])
        for stem_variant in (0, 1):
            questions.append(build_question_record(item, q_no, stem_variant, subject, appearance_days))
            q_no += 1

    session = {
        "key": lib.session_key(day, subject),
        "kind": "daily",
        "day": day,
        "subject": subject,
        "focus": focus,
        "priority": priority,
        "priority_summary": pack.infer_session_priority_summary(subject, items),
        "question_count": len(questions),
        "display_name": f"Day {day:02d}｜科目 {subject}",
        "question_file": f"daily/day-{day:02d}-subject-{subject}.md",
        "attempt_file": f"attempts/day-{day:02d}-subject-{subject}-attempt.md",
        "report_file": f"reports/day-{day:02d}-subject-{subject}-report.md",
        "source_tier": "official-derived",
        "source_refs": ["sources/official-corpus.md", "sources/scope-weight-map.md"],
        "evidence_tags": ["official-scope", "official-sample", "official-announcement"],
        "score_command": f"python .\\score_attempt.py --day {day} --subject {subject}",
        "questions": questions,
    }
    session["session_version"] = compute_session_version(session["key"], session["focus"], session["questions"])
    return session


def build_extended_session(drill_payload: dict) -> dict:
    subject = drill_payload["subject"]
    priority = expanded.drill_priority(drill_payload)
    questions = []
    q_no = 1
    for item in drill_payload["items"]:
        for stem_variant in (0, 1):
            questions.append(build_question_record(item, q_no, stem_variant, subject, []))
            q_no += 1

    key = drill_payload["key"]
    session = {
        "key": key,
        "kind": "extended",
        "day": None,
        "subject": subject,
        "focus": drill_payload["focus"],
        "priority": priority,
        "priority_summary": expanded.drill_priority_summary(drill_payload),
        "question_count": len(questions),
        "display_name": drill_payload["title"],
        "recommended_after": drill_payload["recommended_after"],
        "question_file": f"extended/{key}.md",
        "attempt_file": f"attempts/{key}-attempt.md",
        "report_file": f"reports/{key}-report.md",
        "source_tier": expanded.drill_source_tier(drill_payload),
        "source_refs": expanded.drill_source_refs(drill_payload),
        "evidence_tags": expanded.drill_evidence_tags(drill_payload),
        "score_command": f"python .\\score_attempt.py --drill {key}",
        "questions": questions,
    }
    session["session_version"] = compute_session_version(session["key"], session["focus"], session["questions"])
    return session


def build_manifest() -> dict:
    sessions = []
    for day in range(1, 21):
        for subject in (1, 2):
            sessions.append(build_daily_session(day, subject))
    for drill_payload in expanded.DRILLS:
        sessions.append(build_extended_session(drill_payload))
    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "pack_schema_version": "2026-04-28-a",
        "priority_scheme_version": "2026-04-27-a",
        "sessions": sessions,
    }


def render_readme() -> str:
    return dedent(
        """
        # iPAS 中級 AI 規劃師 20 天反向刷題包

        這個 workspace 已經整理成可直接作答、批改、追蹤弱點的格式。

        - [study-hub.md](study-hub.md)：主入口，含 20 天每日題單與 extended 加練
        - `daily/`：每日正式題單
        - `extended/`：額外加練題庫
        - `attempts/`：作答單
        - `reports/`：批改報告
        - `progress/`：成績、弱點、回看佇列
        - `data/pack-manifest.json`：題單結構與正解索引

        ## 優先級說明

        - `A`：先刷。高命中主戰場，優先來自官方範圍、官方樣題、官方公告題型。
        - `B`：第二層。常見延伸題型，通常用來補回鍋與跨章情境。
        - `C`：最後補。低報酬或偏補洞題，不影響 20 天過線主路徑。

        ## 來源層級

        - `official-derived`：依官方範圍、官方樣題、官方公告題型轉寫。
        - `public-pattern-derived`：依公開練習題、備考心得、非官方題型整理轉寫。
        - 題目不直接照抄網路題面；公開來源只用來抽題型與干擾選項邏輯。

        ## 重建整包

        ```powershell
        python .\\build_full_pack.py
        ```

        ## 批改每日題單

        ```powershell
        python .\\score_attempt.py --day 1 --subject 1
        ```

        也可以直接貼答案：

        ```powershell
        python .\\score_attempt.py --day 1 --subject 1 --answers D,A,C,B,D,A,C,B
        ```

        ## 批改 extended 加練

        ```powershell
        python .\\score_attempt.py --drill subject-2-code-practice-drill
        ```

        ## Extended 題庫入口

        - [extended/README.md](extended/README.md)
        """
    ).strip() + "\n"


def render_study_hub(manifest: dict) -> str:
    session_lookup = lib.session_map(manifest)
    daily_rows = []
    for day in range(1, 21):
        s1 = session_lookup[lib.session_key(day, 1)]
        s2 = session_lookup[lib.session_key(day, 2)]
        daily_rows.append(
            f"| Day {day:02d} | {s1['focus']} | `{s1['priority']}` | "
            f"[題目](./{s1['question_file']}) / [作答](./{s1['attempt_file']}) / [報告](./{s1['report_file']}) | "
            f"{s2['focus']} | `{s2['priority']}` | [題目](./{s2['question_file']}) / [作答](./{s2['attempt_file']}) / [報告](./{s2['report_file']}) |"
        )

    extended_rows = []
    for drill_payload in expanded.DRILLS:
        session = session_lookup[drill_payload["key"]]
        extended_rows.append(
            f"| {session['display_name']} | 科目 {session['subject']} | `{session['priority']}` | `{session['source_tier']}` | {session['focus']} | "
            f"{session['recommended_after']} | "
            f"[題目](./{session['question_file']}) / [作答](./{session['attempt_file']}) / [報告](./{session['report_file']}) |"
        )

    return "\n".join(
        [
            "# Study Hub",
            "",
            "## 使用方式",
            "",
            "1. 先開 `daily/` 或 `extended/` 題單直接做題。",
            "2. 到 `attempts/` 填作答單，或直接用 `--answers` 批改。",
            "3. 執行 `python .\\score_attempt.py ...` 產生報告。",
            "4. 回看 `progress/scoreboard.md`、`progress/auto-knowledge-gaps.md`、`progress/auto-review-queue.md`。",
            "",
            "## 核心資料",
            "",
            "- [官方來源整理](./sources/official-corpus.md)",
            "- [L-code 權重地圖](./sources/scope-weight-map.md)",
            "- [題源與轉寫規則](./sources/question-source-map.md)",
            "- [每日回看索引](./progress/daily-review-index.md)",
            "- [成績總表](./progress/scoreboard.md)",
            "- [自動弱點](./progress/auto-knowledge-gaps.md)",
            "- [回看順序](./progress/auto-review-queue.md)",
            "- [Extended 題庫](./extended/README.md)",
            "",
            "## 20 天每日題單",
            "",
            "| 天數 | 科目 1 焦點 | 科目 1 優先級 | 科目 1 | 科目 2 焦點 | 科目 2 優先級 | 科目 2 |",
            "| --- | --- | --- | --- | --- | --- | --- |",
            *daily_rows,
            "",
            "## Extended 加練",
            "",
            "| 題庫 | 科目 | 優先級 | 來源層級 | 焦點 | 建議加做時機 | 入口 |",
            "| --- | --- | --- | --- | --- | --- | --- |",
            *extended_rows,
            "",
        ]
    )


def render_attempt_template(session: dict) -> str:
    lines = [
        f"<!-- attempt-template session-key={session['key']} session-version={session.get('session_version', '-') } -->",
        f"# {session['display_name']}｜作答單",
        "",
        f"- 類型：`{lib.session_kind_label(session)}`",
        f"- 焦點：`{session['focus']}`",
        f"- 優先級：`{session.get('priority', '-')}`",
        f"- 來源層級：`{session.get('source_tier', '-')}`",
        f"- 題庫版本：`{session.get('session_version', '-')}`",
        f"- 題目：[{Path(session['question_file']).name}](../{session['question_file']})",
        f"- 報告：[{Path(session['report_file']).name}](../{session['report_file']})",
        f"- 批改指令：`{session['score_command']}`",
        "- 快速批改語法：`python .\\score_attempt.py ... --answers A,B,C,D,...`",
        "- `--answers` 只接受 `A/B/C/D`，不要保留 `?` 或其他占位字。",
    ]

    if session.get("kind") == "extended":
        lines.append(f"- 建議加做時機：`{session['recommended_after']}`")

    lines.extend(
        [
            "",
            "## 作答表",
            "",
            "| 題號 | 你的答案 | 把握度 | 能否解釋 | 備註 |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for q_no in range(1, session["question_count"] + 1):
        lines.append(f"| {q_no} |  |  |  |  |")

    lines.extend(
        [
            "",
            "## 可直接貼到命令列的答案字串",
            "",
            "把下行改成你的真實答案後，再貼給 `--answers` 使用：",
            "A,B,C,D,...",
            "",
            "## 填寫規則",
            "",
            "- `把握度` 只接受：`高 / 中 / 低`",
            "- `能否解釋` 只接受：`是 / 否`",
            "- 如果你只想快速批改，也可以只填答案欄，其餘留空。",
            "",
        ]
    )
    return "\n".join(lines)


def render_attempts_index(manifest: dict) -> str:
    daily_rows = []
    extended_rows = []

    for session in manifest["sessions"]:
        row = (
            f"| {session['display_name']} | `{session.get('priority', '-')}` | {session['focus']} | "
            f"[作答單](./{Path(session['attempt_file']).name}) | "
            f"[報告](../{session['report_file']}) |"
        )
        if session.get("kind") == "daily":
            daily_rows.append(row)
        else:
            extended_rows.append(row)

    lines = [
        "# Attempts Index",
        "",
        "## 每日題單",
        "",
        "| 題單 | 優先級 | 焦點 | 作答 | 報告 |",
        "| --- | --- | --- | --- | --- |",
        *daily_rows,
        "",
    ]

    if extended_rows:
        lines.extend(
            [
                "## Extended 加練",
                "",
                "| 題單 | 優先級 | 焦點 | 作答 | 報告 |",
                "| --- | --- | --- | --- | --- |",
                *extended_rows,
                "",
            ]
        )

    return "\n".join(lines)


def render_question_source_map() -> str:
    return dedent(
        """
        # Question Source Map

        這份文件整理「題庫可以參考哪些來源」以及「哪些只能抽題型、不能近似改寫」。

        ## A 級必擴

        - [官方試題與樣題總入口](https://www.ipas.org.tw/AIAP/AbilityPageContent.aspx?pgeno=4de5cc7f-a878-43bd-bd6f-ee11ea40be1c)
        - [中級樣題 114.09](https://www.ipas.org.tw/DownloadFile.ashx?filename=4002eaa2-bfea-400e-abd1-2f4c1a1f8de8_iPAS+AI%E6%87%89%E7%94%A8%E8%A6%8F%E5%8A%83%E5%B8%AB%E4%B8%AD%E7%B4%9A%E8%83%BD%E5%8A%9B%E9%91%91%E5%AE%9A-%E8%80%83%E8%A9%A6%E6%A8%A3%E9%A1%8C%28114%E5%B9%B49%E6%9C%88%E7%89%88%29+_v2.pdf&type=10)
        - [114 年第二梯次中級科目 2 公告試題](https://www.ipas.org.tw/DownloadFile.ashx?filename=8840cc98-928c-4ded-b546-b6bb8f5537eb_114%E5%B9%B4%E7%AC%AC%E4%BA%8C%E6%A2%AF%E6%AC%A1%E4%B8%AD%E7%B4%9AAI%E6%87%89%E7%94%A8%E8%A6%8F%E5%8A%83%E5%B8%AB_%E7%AC%AC%E4%BA%8C%E7%A7%91_%E5%A4%A7%E6%95%B8%E6%93%9A%E8%99%95%E7%90%86%E5%88%86%E6%9E%90%E8%88%87%E6%87%89%E7%94%A8%28%E7%95%B6%E6%AC%A1%E8%A9%A6%E9%A1%8C%E5%85%AC%E5%91%8A114.11.20%29.pdf&type=10)
        - [114 年第二梯次中級科目 1 公告試題](https://www.ipas.org.tw/DownloadFile.ashx?filename=28a0c0d2-2165-45fe-994d-df07dc0eb50e_114%E5%B9%B4%E7%AC%AC%E4%BA%8C%E6%A2%AF%E6%AC%A1%E4%B8%AD%E7%B4%9AAI%E6%87%89%E7%94%A8%E8%A6%8F%E5%8A%83%E5%B8%AB_%E7%AC%AC%E4%B8%80%E7%A7%91_%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%8A%80%E8%A1%93%E6%87%89%E7%94%A8%E8%88%87%E8%A6%8F%E5%8A%83%28%E7%95%B6%E6%AC%A1%E8%A9%A6%E9%A1%8C%E5%85%AC%E5%91%8A114.11.20%29.pdf&type=10)
        - [評鑑內容範圍參考 114.04](https://www.ipas.org.tw/DownloadFile.ashx?filename=14ae134c-fb2f-4741-9f6d-062c02bdbc94_AI%E6%87%89%E7%94%A8%E8%A6%8F%E5%8A%83%E5%B8%AB%E8%83%BD%E5%8A%9B%E9%91%91%E5%AE%9A_%E8%A9%95%E9%91%91%E5%85%A7%E5%AE%B9%E7%AF%84%E5%9C%8D%E5%8F%83%E8%80%83_11404.pdf&type=10)
        - [Python 題型公告](https://www.ipas.org.tw/AIAP/AbilityNewsData.aspx?nwsno=a443b352-e677-4e4f-9b27-0fc0d7c23d02)
        - [中級學習指引科目 1](https://www.ipas.org.tw/DownloadFile.ashx?filename=274eb504-3b33-4643-9ca4-7f3707daa974_AI%E6%87%89%E7%94%A8%E8%A6%8F%E5%8A%83%E5%B8%AB%28%E4%B8%AD%E7%B4%9A%29-%E5%AD%B8%E7%BF%92%E6%8C%87%E5%BC%95-%E7%A7%91%E7%9B%AE1_%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7%E6%8A%80%E8%A1%93%E6%87%89%E7%94%A8%E8%A6%8F%E5%8A%83.pdf&type=10)
        - [中級學習指引科目 2](https://www.ipas.org.tw/DownloadFile.ashx?filename=f611f4cf-5f7a-4995-a074-b1f01f210d3d_AI%E6%87%89%E7%94%A8%E8%A6%8F%E5%8A%83%E5%B8%AB%28%E4%B8%AD%E7%B4%9A%29-%E5%AD%B8%E7%BF%92%E6%8C%87%E5%BC%95-%E7%A7%91%E7%9B%AE2_%E5%A4%A7%E6%95%B8%E6%93%9A%E8%99%95%E7%90%86%E5%88%86%E6%9E%90%E8%88%87%E6%87%89%E7%94%A8.pdf&type=10)

        ## B 級可擴

        - [AITerms Python 題攻略](https://aiterms.tw/ipas/guide/ipas-python-guide/)
        - [AITerms 範圍整理](https://aiterms.tw/ipas/scope/)
        - [S 測驗中級科目 2 模擬題](https://sustainnovation.cc/ipas-ai%e6%87%89%e7%94%a8%e8%a6%8f%e5%8a%83%e5%b8%ab%e4%b8%ad%e7%b4%9a-%e7%a7%91%e7%9b%ae2-%e5%a4%a7%e6%95%b8%e6%93%9a%e8%99%95%e7%90%86%e5%88%86%e6%9e%90%e8%88%87%e6%87%89%e7%94%a8-%e6%a8%a1/)
        - [S 測驗中級題庫索引](https://sustainnovation.cc/courses/ipas-ai-two/)
        - [CCChen 科目 2 模擬題](https://vocus.cc/article/68b948cbfd897800019ee2a3)
        - [CCChen 科目 1 模擬題](https://vocus.cc/article/68b94606fd897800019dff1d)
        - [CCChen 中級學習指引整理](https://vocus.cc/article/68ecd196fd89780001f5c8f1)

        ## C 級只當熱點雷達

        - [iPAS 練功房](https://ipas-ai.net/)
        - [CCChen 114-2 考試分析](https://vocus.cc/article/6910a926fd89780001452b48)

        ## 轉寫規則

        - 官方題與樣題只拿來學題型骨架、主題熱區、干擾選項邏輯。
        - 不保留原情境名詞、原數字、原資料表或原選項句式。
        - 公開練習題與心得頁只做靈感來源，不直接改寫成近似題面。
        - 有登入、付費或完整題解的平台，只當熱點雷達，不當直接題源。
        """
    ).strip() + "\n"


def attempt_sheet_is_blank(path: Path) -> bool:
    parsed = lib.parse_attempt_markdown(path)
    return (
        not any(parsed["answers"])
        and not any(parsed["confidence"])
        and not any(parsed["explain"])
        and not any(note.strip() for note in parsed["notes"])
    )


def build_static_files() -> None:
    pack.generate()
    expanded.generate_extended_drills()

    manifest = build_manifest()
    lib.write_json(lib.MANIFEST_PATH, manifest)

    lib.write_text(ROOT / "sources" / "question-source-map.md", render_question_source_map())
    lib.write_text(ROOT / "README.md", render_readme())
    lib.write_text(ROOT / "study-hub.md", render_study_hub(manifest))
    lib.write_text(lib.ATTEMPTS_DIR / "README.md", render_attempts_index(manifest))

    if not lib.ATTEMPT_LOG_PATH.exists():
        lib.save_attempt_log({"attempts": []})
    attempt_log = lib.load_attempt_log()
    latest_attempts = lib.latest_attempts_by_key(attempt_log, lib.session_version_map(manifest))

    lib.write_text(lib.PROGRESS_DIR / "scoreboard.md", lib.render_scoreboard(manifest, attempt_log))
    lib.write_text(lib.PROGRESS_DIR / "auto-knowledge-gaps.md", lib.render_auto_knowledge_gaps(manifest, attempt_log))
    lib.write_text(lib.PROGRESS_DIR / "auto-review-queue.md", lib.render_auto_review_queue(manifest, attempt_log))

    for session in manifest["sessions"]:
        attempt_path = ROOT / session["attempt_file"]
        if attempt_path.exists() and not attempt_sheet_is_blank(attempt_path) and attempt_sheet_needs_refresh(attempt_path, session):
            backup_stale_attempt(attempt_path)
        if attempt_sheet_needs_refresh(attempt_path, session):
            lib.write_text(attempt_path, render_attempt_template(session))

        report_path = ROOT / session["report_file"]
        latest_attempt = latest_attempts.get(session["key"])
        if latest_attempt is None:
            lib.write_text(report_path, lib.render_placeholder_report(session))
        else:
            lib.write_text(report_path, lib.render_attempt_report(session, latest_attempt))


if __name__ == "__main__":
    build_static_files()
