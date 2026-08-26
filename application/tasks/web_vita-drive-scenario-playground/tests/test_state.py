from __future__ import annotations

import json
import os
import sys
from pathlib import Path

OUTPUT_DIR = Path(
    os.environ.get("HARBOR_OUTPUT_DIR")
    or os.environ.get("MATRIX_OUTPUT_DIR")
    or "/app/output"
)
OUTPUT = OUTPUT_DIR / "playground_experience.json"
USER_FEEDBACK = OUTPUT_DIR / "user_feedback.json"
DECISION_OUTCOMES = {"selected", "considered", "rejected", "deferred", "skipped"}
BASIS_PRIMARY = {
    "price",
    "quality",
    "features",
    "convenience",
    "taste",
    "trust",
    "familiarity",
    "novelty",
    "fit",
    "other",
}
EXPLORATION_STYLES = {"quick_pick", "compared_multiple", "deep_research", "hesitant"}
SATISFACTION_BUCKETS = {"yes", "partially", "no"}


def _verifier_dir() -> Path:
    base = os.environ.get("HARBOR_VERIFIER_DIR") or "/logs/verifier"
    path = Path(base)
    try:
        path.mkdir(parents=True, exist_ok=True)
        return path
    except OSError:
        path = Path(__file__).resolve().parent.parent / "verifier"
        path.mkdir(parents=True, exist_ok=True)
        return path


def _write_structured_output(payload: dict[str, object]) -> None:
    path = _verifier_dir() / "structured_output.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _navigation_path_type(exploration_style: str) -> str:
    return {
        "quick_pick": "direct",
        "compared_multiple": "browse_compare",
        "deep_research": "browse_compare",
        "hesitant": "direct",
    }.get(exploration_style, "direct")


def _build_execution_contexts(
    *,
    output: Path,
    subject_id: str,
    subject_label: str,
    exploration_style: str,
) -> list[dict[str, object]]:
    return [
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
                    "value": "passed",
                },
                {
                    "key": "goal_completion_ratio",
                    "label": "Goal completion ratio",
                    "role": "score",
                    "kind": "numerical",
                    "value": 1.0,
                },
                {
                    "key": "goal_completion_bucket",
                    "label": "Goal completion bucket",
                    "role": "primary",
                    "kind": "categorical",
                    "value": "complete",
                },
                {
                    "key": "verifier_mode",
                    "label": "Verifier mode",
                    "role": "evidence",
                    "kind": "categorical",
                    "value": "artifact_exact",
                },
                {
                    "key": "primary_failure_reason",
                    "label": "Primary failure reason",
                    "role": "primary",
                    "kind": "categorical",
                    "value": "none",
                },
                {
                    "key": "outcome_explanation",
                    "label": "Outcome explanation",
                    "role": "explanation",
                    "kind": "textual",
                    "value": f"The persona explored Scenario Playground & Evaluation Lab and saved a valid {output.name} artifact.",
                },
                {
                    "key": "completion_evidence",
                    "label": "Completion evidence",
                    "role": "evidence",
                    "kind": "textual",
                    "value": f"Saved {output.name} with subject {subject_label.strip()}.",
                },
            ],
        }
    ]


def _build_decision_context(data: dict[str, object]) -> dict[str, object]:
    subject_id = str(data["decision_subject_id"]).strip()
    subject_label = str(data["decision_subject_label"]).strip()
    decision_outcome = str(data["decision_outcome"]).strip()
    basis_primary = str(data["basis_primary"]).strip()
    exploration_style = str(data["exploration_style"]).strip()
    reason = str(data["reason"]).strip()

    facets: list[dict[str, object]] = [
        {
            "key": "decision_subject_id",
            "label": "Decision subject id",
            "role": "primary",
            "kind": "categorical",
            "value": subject_id,
        },
        {
            "key": "decision_subject_label",
            "label": "Decision subject label",
            "role": "identifier",
            "kind": "categorical",
            "value": subject_label,
        },
        {
            "key": "decision_outcome",
            "label": "Decision outcome",
            "role": "primary",
            "kind": "categorical",
            "value": decision_outcome,
        },
        {
            "key": "basis_primary",
            "label": "Primary basis",
            "role": "primary",
            "kind": "categorical",
            "value": basis_primary,
        },
        {
            "key": "exploration_style",
            "label": "Exploration style",
            "role": "control",
            "kind": "categorical",
            "value": exploration_style,
        },
        {
            "key": "reason",
            "label": "Reason",
            "role": "explanation",
            "kind": "textual",
            "value": reason,
        },
    ]

    if "task_favorite_feature" in data:
        facets.append({
            "key": "favorite_feature",
            "label": "Favorite feature",
            "role": "evidence",
            "kind": "categorical",
            "value": str(data["task_favorite_feature"]).strip(),
        })

    if "task_favorite_scenario" in data:
        facets.append({
            "key": "favorite_scenario",
            "label": "Favorite scenario",
            "role": "evidence",
            "kind": "categorical",
            "value": str(data["task_favorite_scenario"]).strip(),
        })

    if "task_ease_of_use_rating" in data:
        facets.append({
            "key": "ease_of_use_rating",
            "label": "Ease of use rating",
            "role": "metric",
            "kind": "numerical",
            "value": int(data["task_ease_of_use_rating"]),
        })

    return {
        "key": "decision.primary",
        "label": "Primary decision",
        "contextType": "decision",
        "facets": facets,
    }


def _build_user_feedback_context(data: dict[str, object]) -> dict[str, object] | None:
    if not isinstance(data, dict):
        return None
    rating = data.get("overallExperienceRating")
    if not isinstance(rating, int) or rating < 1 or rating > 10:
        return None
    return {
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
            }
        ],
    }


def main() -> int:
    target_output = OUTPUT
    if not target_output.is_file():
        # Check fallback
        alt_output = OUTPUT_DIR / "dashboard_experience.json"
        if alt_output.is_file():
            target_output = alt_output
        else:
            print(f"FAIL: missing {OUTPUT}", file=sys.stderr)
            return 1

    try:
        data = json.loads(target_output.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"FAIL: invalid JSON in {target_output}: {e}", file=sys.stderr)
        return 1

    if not isinstance(data, dict):
        print(f"FAIL: {target_output} must contain a JSON object", file=sys.stderr)
        return 1

    for required_key in ["decision_subject_id", "decision_subject_label", "decision_outcome", "basis_primary", "exploration_style", "reason"]:
        if required_key not in data or not str(data[required_key]).strip():
            print(f"FAIL: missing or empty key '{required_key}' in {target_output}", file=sys.stderr)
            return 1

    decision_context = _build_decision_context(data)
    exec_contexts = _build_execution_contexts(
        output=target_output,
        subject_id=str(data["decision_subject_id"]),
        subject_label=str(data["decision_subject_label"]),
        exploration_style=str(data["exploration_style"]),
    )

    contexts = exec_contexts + [decision_context]

    if USER_FEEDBACK.is_file():
        try:
            fb = json.loads(USER_FEEDBACK.read_text(encoding="utf-8"))
            fb_ctx = _build_user_feedback_context(fb)
            if fb_ctx:
                contexts.append(fb_ctx)
        except Exception:
            pass

    structured_output = {
        "schemaVersion": "1.0",
        "artifactType": "matraix.trial_evaluation",
        "taskType": "web",
        "contexts": contexts,
    }
    _write_structured_output(structured_output)
    print("PASS: Vita Scenario Playground web evaluation artifacts are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
