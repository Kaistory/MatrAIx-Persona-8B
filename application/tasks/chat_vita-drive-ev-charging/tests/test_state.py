from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any

OUTPUT_DIR = Path(
    os.environ.get("HARBOR_OUTPUT_DIR")
    or os.environ.get("MATRIX_OUTPUT_DIR")
    or "/app/output"
)
TRANSCRIPT_PATH = OUTPUT_DIR / "transcript.json"
FEEDBACK_PATH = OUTPUT_DIR / "user_feedback.json"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def _verifier_dir() -> Path:
    explicit = os.environ.get("HARBOR_VERIFIER_DIR")
    if explicit:
        path = Path(explicit)
        path.mkdir(parents=True, exist_ok=True)
        return path

    container_default = Path("/logs/verifier")
    try:
        container_default.mkdir(parents=True, exist_ok=True)
        return container_default
    except OSError:
        pass

    raise RuntimeError(
        "HARBOR_VERIFIER_DIR is required when running outside a Harbor trial "
        "container. Point it at jobs/<job>/<trial>/verifier for local harness runs."
    )


def load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        fail(f"{path} is missing")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path} is not valid JSON: {exc}")
    if not isinstance(value, dict):
        fail(f"{path} must contain a JSON object")
    return value


def require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(f"{label} must be a non-empty string")
    return value


def _normalize_feedback_bucket(value: Any, label: str) -> str:
    text = str(value).strip().lower()
    if text in {"true", "1"}:
        return "yes"
    if text in {"false", "0"}:
        return "no"
    if text not in {"yes", "partially", "no"}:
        fail(f"{label} must be one of yes / partially / no")
    return text


def _bool_category(value: bool) -> str:
    return "true" if value else "false"


def _support_messages(messages: list[dict[str, Any]]) -> list[str]:
    return [
        entry["content"].strip()
        for entry in messages
        if entry.get("role") in {"support", "assistant", "system"}
        and isinstance(entry.get("content"), str)
        and entry["content"].strip()
    ]


def _derive_outcome_status_from_feedback(
    need_satisfaction: str,
    preference_satisfaction: str,
) -> str:
    if need_satisfaction == "yes" and preference_satisfaction == "yes":
        return "resolved"
    if need_satisfaction == "no":
        return "unresolved"
    return "partially_resolved"


def validate_transcript(data: dict[str, Any]) -> tuple[list[dict[str, Any]], str]:
    messages = data.get("messages")
    if not isinstance(messages, list) or not messages:
        fail("transcript.messages must be a non-empty list")
    for entry in messages:
        if entry.get("role") not in {"customer", "user", "support", "assistant"}:
            fail("invalid transcript message role")
        require_string(entry.get("content"), "message content")
    combined = " ".join(str(entry["content"]) for entry in messages)
    return messages, combined


def validate_feedback(feedback: dict[str, Any]) -> None:
    for key in ("needConstraintSatisfaction", "personalPreferenceSatisfaction"):
        if feedback.get(key) in (None, ""):
            fail(f"user_feedback.{key} must be present")
    require_string(feedback.get("reason"), "user_feedback.reason")
    rating = feedback.get("overallExperienceRating")
    if not isinstance(rating, int) or rating < 1 or rating > 10:
        fail("user_feedback.overallExperienceRating must be an integer 1-10")
    asked = feedback.get("askedUsefulClarificationQuestions")
    if not isinstance(asked, bool):
        fail("user_feedback.askedUsefulClarificationQuestions must be boolean")


def build_evaluation_payload(
    messages: list[dict[str, Any]],
    combined: str,
    feedback: dict[str, Any] | None,
) -> dict[str, Any]:
    customer_count = sum(1 for message in messages if message.get("role") in {"customer", "user"})
    support_count = sum(1 for message in messages if message.get("role") in {"support", "assistant"})

    rating: int | None = None
    need_satisfaction: str | None = None
    preference_satisfaction: str | None = None
    clarification_useful: str | None = None
    feedback_reason: str | None = None

    if feedback is not None:
        validate_feedback(feedback)
        rating = int(feedback["overallExperienceRating"])
        need_satisfaction = _normalize_feedback_bucket(
            feedback.get("needConstraintSatisfaction"),
            "user_feedback.needConstraintSatisfaction",
        )
        preference_satisfaction = _normalize_feedback_bucket(
            feedback.get("personalPreferenceSatisfaction"),
            "user_feedback.personalPreferenceSatisfaction",
        )
        clarification_useful = _bool_category(
            bool(feedback.get("askedUsefulClarificationQuestions"))
        )
        feedback_reason = require_string(feedback.get("reason"), "user_feedback.reason")
        outcome_status = _derive_outcome_status_from_feedback(
            need_satisfaction,
            preference_satisfaction,
        )
        resolution_basis = "user_feedback"
        outcome_reason = feedback_reason
    else:
        outcome_status = "partially_resolved" if support_count >= 2 else "unresolved"
        resolution_basis = "conversation_commitment"
        outcome_reason = "Conversation completed without explicit user feedback."

    payload: dict[str, Any] = {
        "schemaVersion": "1.0",
        "artifactType": "matraix.trial_evaluation",
        "contexts": [
            {
                "key": "task_outcome.primary",
                "label": "Task outcome",
                "contextType": "task_outcome",
                "facets": [
                    {
                        "key": "outcome_status",
                        "label": "Outcome status",
                        "role": "primary",
                        "kind": "categorical",
                        "value": outcome_status,
                    },
                    {
                        "key": "resolution_basis",
                        "label": "Resolution basis",
                        "role": "control",
                        "kind": "categorical",
                        "value": resolution_basis,
                    },
                    {
                        "key": "customer_message_count",
                        "label": "Customer messages",
                        "role": "metric",
                        "kind": "continuous",
                        "value": customer_count,
                    },
                    {
                        "key": "support_message_count",
                        "label": "Vita assistant messages",
                        "role": "metric",
                        "kind": "continuous",
                        "value": support_count,
                    },
                    {
                        "key": "outcome_reason",
                        "label": "Outcome reason",
                        "role": "explanation",
                        "kind": "textual",
                        "value": outcome_reason,
                    },
                ],
            }
        ],
    }

    if feedback is not None:
        payload["contexts"].append(
            {
                "key": "user_feedback.primary",
                "label": "User feedback",
                "contextType": "user_feedback",
                "facets": [
                    {
                        "key": "overall_experience_rating",
                        "label": "Overall experience rating",
                        "role": "primary",
                        "kind": "continuous",
                        "value": rating,
                    },
                    {
                        "key": "clarification_questions_useful",
                        "label": "Clarification / confirmation useful",
                        "role": "primary",
                        "kind": "categorical",
                        "value": clarification_useful,
                    },
                    {
                        "key": "need_constraint_satisfaction",
                        "label": "Need satisfaction",
                        "role": "evidence",
                        "kind": "categorical",
                        "value": need_satisfaction,
                    },
                    {
                        "key": "personal_preference_satisfaction",
                        "label": "Preference satisfaction",
                        "role": "evidence",
                        "kind": "categorical",
                        "value": preference_satisfaction,
                    },
                ],
            }
        )

    return payload


def main() -> int:
    transcript = load_json(TRANSCRIPT_PATH)
    messages, combined = validate_transcript(transcript)
    feedback = load_json(FEEDBACK_PATH) if FEEDBACK_PATH.is_file() else None
    payload = build_evaluation_payload(messages, combined, feedback)
    (_verifier_dir() / "structured_output.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print("PASS: Vita EV Charging & Energy chat artifacts are valid")
    return 0


def test_transcript_exists() -> None:
    assert TRANSCRIPT_PATH.is_file(), f"Missing {TRANSCRIPT_PATH}"


def test_transcript_schema() -> None:
    transcript = load_json(TRANSCRIPT_PATH)
    messages, combined = validate_transcript(transcript)
    feedback = load_json(FEEDBACK_PATH) if FEEDBACK_PATH.is_file() else None
    payload = build_evaluation_payload(messages, combined, feedback)
    assert payload["contexts"], "Evaluation payload must contain contexts"


if __name__ == "__main__":
    raise SystemExit(main())
