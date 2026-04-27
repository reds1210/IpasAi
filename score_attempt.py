from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

import study_pack_lib as lib


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Score iPAS reverse-practice attempt sheets.")
    parser.add_argument("--day", type=int, help="Study day number, e.g. 1")
    parser.add_argument("--subject", type=int, choices=[1, 2], help="Subject number: 1 or 2")
    parser.add_argument("--drill", type=str, help="Extended drill key, e.g. subject-2-code-practice-drill")
    parser.add_argument("--file", type=str, help="Path to attempt markdown file. Defaults to the manifest path for that session.")
    parser.add_argument("--answers", type=str, help="Inline answer string, e.g. A,B,C,D")
    parser.add_argument("--dry-run", action="store_true", help="Score and print summary without writing logs or reports")
    return parser


def resolve_session(args: argparse.Namespace, sessions: dict[str, dict]) -> dict:
    if args.drill:
        if args.day is not None or args.subject is not None:
            raise ValueError("Use either --drill or --day/--subject, not both.")
        session = sessions.get(args.drill)
        if session is None:
            raise KeyError(f"extended drill not found: {args.drill}")
        return session

    if args.day is None or args.subject is None:
        raise ValueError("Daily scoring requires both --day and --subject.")

    key = lib.session_key(args.day, args.subject)
    session = sessions.get(key)
    if session is None:
        raise KeyError(f"session not found: {key}")
    return session


def default_attempt_path(session: dict) -> Path:
    return lib.ROOT / session["attempt_file"]


def resolve_answers(session: dict, answers_blob: str | None, file_arg: str | None) -> tuple[list[str], list[str], list[str], list[str], str]:
    if answers_blob:
        answers, invalid = lib.parse_inline_answer_blob(answers_blob)
        if invalid:
            raise ValueError("inline answers 含有非法值，只接受 A/B/C/D：" + ", ".join(invalid))
        return answers, [""] * len(answers), [""] * len(answers), [""] * len(answers), "inline"

    file_path = Path(file_arg) if file_arg else default_attempt_path(session)
    if not file_path.exists():
        raise FileNotFoundError(f"attempt file not found: {file_path}")
    parsed = lib.parse_attempt_markdown(file_path)
    if parsed.get("session_version") and parsed["session_version"] != session.get("session_version"):
        raise ValueError(
            "attempt sheet version mismatch. Run `python .\\build_full_pack.py` to refresh the template, "
            f"then retry. file={parsed['session_version']} current={session.get('session_version')}"
        )
    if parsed["errors"]:
        raise ValueError("\n".join(parsed["errors"]))
    return parsed["answers"], parsed["confidence"], parsed["explain"], parsed["notes"], str(file_path)


def score_session(session: dict, answers: list[str], confidence: list[str], explain: list[str], notes: list[str], source: str) -> dict:
    expected_count = session["question_count"]
    if len(answers) != expected_count:
        raise ValueError(
            f"expected {expected_count} answers, got {len(answers)}. "
            "The attempt sheet may be outdated; run `python .\\build_full_pack.py` to refresh it."
        )

    results = []
    correct_count = 0
    for idx, question in enumerate(session["questions"]):
        selected = answers[idx] if idx < len(answers) else ""
        user_confidence = confidence[idx] if idx < len(confidence) else ""
        can_explain = explain[idx] if idx < len(explain) else ""
        note = notes[idx] if idx < len(notes) else ""
        is_correct = selected == question["correct"]
        if is_correct:
            correct_count += 1
        results.append(
            {
                "question_no": question["question_no"],
                "selected": selected,
                "correct": question["correct"],
                "confidence": user_confidence,
                "can_explain": can_explain,
                "note": note,
                "is_correct": is_correct,
            }
        )

    score_pct = (correct_count / expected_count) * 100
    submitted_at = datetime.now().astimezone().isoformat(timespec="seconds")
    return {
        "session_key": session["key"],
        "session_version": session.get("session_version", ""),
        "kind": session.get("kind", "daily"),
        "day": session.get("day"),
        "subject": session["subject"],
        "label": session.get("display_name", session["key"]),
        "source": source,
        "submitted_at": submitted_at,
        "correct_count": correct_count,
        "total_questions": expected_count,
        "score_pct": score_pct,
        "question_results": results,
    }


def print_summary(session: dict, attempt: dict) -> None:
    status = "PASS" if attempt["score_pct"] >= 70 else "REVIEW"
    print(
        f"{session.get('display_name', session['key'])} | "
        f"{attempt['correct_count']}/{attempt['total_questions']} | "
        f"{attempt['score_pct']:.1f}% | {status}"
    )


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    manifest = lib.load_manifest()
    sessions = lib.session_map(manifest)
    session = resolve_session(args, sessions)

    answers, confidence, explain, notes, source = resolve_answers(session, args.answers, args.file)
    attempt = score_session(session, answers, confidence, explain, notes, source)
    print_summary(session, attempt)

    if args.dry_run:
        return

    attempt_log = lib.load_attempt_log()
    attempt_log.setdefault("attempts", []).append(attempt)
    lib.save_attempt_log(attempt_log)

    report_path = lib.ROOT / session["report_file"]
    lib.write_text(report_path, lib.render_attempt_report(session, attempt))
    lib.write_text(lib.PROGRESS_DIR / "scoreboard.md", lib.render_scoreboard(manifest, attempt_log))
    lib.write_text(lib.PROGRESS_DIR / "auto-knowledge-gaps.md", lib.render_auto_knowledge_gaps(manifest, attempt_log))
    lib.write_text(lib.PROGRESS_DIR / "auto-review-queue.md", lib.render_auto_review_queue(manifest, attempt_log))


if __name__ == "__main__":
    main()
