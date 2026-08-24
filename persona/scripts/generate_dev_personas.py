#!/usr/bin/env python3
"""Write a synthetic persona pool you can pick in Playground Dataset.

Same generate path as Playground: Full-DAG sample, then stamp custom dimensions
into YAML and ``manifest.overlay_dimensions``.

Default: ``--count`` rows (2000) into
``persona/datasets/generated-persona-dev-<count>/``.

``--overlay id[:label]=v1,v2`` adds study dimensions that are not in the persona
schema. ``--filter dim=v1,v2`` constrains schema dims (DAG) and overlay dims
(stamp). ``--per-cell`` / ``--sample-size`` match Playground per-cell / total.

``--strategy PATH`` fills the task's stratified cells so a later Playground draw
will not run short. ``--task PATH --per-cell N`` fills grounding probe cells.
"""

from __future__ import annotations

import argparse
import json
import random
import re
from pathlib import Path

from matraix.persona_dimension_catalog import values_for_dimension
from matraix.persona_generator import (
    GENERATE_COUNT_DEFAULT,
    GENERATE_COUNT_MAX,
    build_probe_strata,
    fill_overlay_filters,
    generate_persona_pool,
    generate_synthetic_personas,
    normalize_overlay_dimensions,
    parse_filter_cli,
    parse_overlay_cli,
    stamp_overlay_independent,
    write_persona_dataset,
)
from matraix.task_catalog import (
    confounder_values_from_grounding,
    get_task_grounding_spec,
    probe_dimension_from_grounding,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
DATASETS_DIR = REPO_ROOT / "persona" / "datasets"
DEFAULT_POOL_PREFIX = "generated-persona-dev"
_DATASETS_SKIP_TOP_LEVEL = frozenset(
    {"_generated", "_sampled", "cohorts", "saved-cohorts", "matraix-persona-1m"}
)


def _default_out_dir(count: int) -> Path:
    return DATASETS_DIR / f"{DEFAULT_POOL_PREFIX}-{count}"


def _strategy_out_dir(task_slug: str) -> Path:
    return DATASETS_DIR / f"{DEFAULT_POOL_PREFIX}-strategy-{task_slug}"


def _is_picker_listed(out: Path) -> bool:
    try:
        rel = out.resolve().relative_to(DATASETS_DIR.resolve())
    except ValueError:
        return False
    return len(rel.parts) == 1 and rel.parts[0] not in _DATASETS_SKIP_TOP_LEVEL


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "strategy"


def _progress(stage: str, message: str) -> None:
    print(f"[{stage}] {message}", flush=True)


def _wipe_stale_personas(out: Path) -> int:
    if not out.is_dir():
        return 0
    removed = 0
    for stale in out.glob("persona_*.yaml"):
        stale.unlink()
        removed += 1
    return removed


def _write_progress(stage: str, payload: dict) -> None:
    label = str(payload.get("label") or stage)
    if stage == "write":
        done = int(payload.get("done") or 0)
        total = int(payload.get("total") or 0)
        if total > 0:
            pct = round(100 * done / total)
            _progress("write", f"{label} ({pct}%)")
            return
    _progress(stage, label)


def _stratum_top_up_from_task(
    task_path: str,
) -> tuple[list[dict[str, str]], dict[str, object]]:
    grounding = get_task_grounding_spec(task_path, repo_root=REPO_ROOT)
    if not grounding:
        raise SystemExit(f"No grounding.toml (or catalog grounding) for {task_path!r}")
    confounders = confounder_values_from_grounding(grounding)
    probe_dimension = probe_dimension_from_grounding(grounding)
    if not confounders or not probe_dimension:
        raise SystemExit(
            f"Task {task_path!r} grounding must define confounders and probe_dimension"
        )
    probe_key = probe_dimension.removeprefix("dimensions.")
    probe_values = values_for_dimension(probe_key)
    if not probe_values:
        raise SystemExit(f"No catalog values for probe dimension {probe_key!r}")
    return build_probe_strata(
        confounders=confounders,
        probe_dimension=probe_dimension,
        probe_values=probe_values,
    ), grounding


def _resolve_strategy_path(raw: str) -> Path:
    path = Path(raw)
    if not path.is_absolute():
        path = REPO_ROOT / path
    if path.is_dir():
        candidate = path / "persona_strategy.json"
        if not candidate.is_file():
            raise SystemExit(f"No persona_strategy.json under {path}")
        return candidate
    if path.is_file():
        return path
    raise SystemExit(f"Strategy path not found: {raw}")


def _load_strategy(path: Path) -> dict[str, object]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Failed to read strategy {path}: {exc}") from exc
    if not isinstance(raw, dict):
        raise SystemExit(f"Strategy {path} must be a JSON object")
    filters = raw.get("dimensionFilters") or {}
    if not isinstance(filters, dict):
        filters = {}
    normalized_filters: dict[str, list[str]] = {}
    for key, values in filters.items():
        dim = str(key).removeprefix("dimensions.").strip()
        if not dim:
            continue
        if isinstance(values, list):
            cleaned = [str(value).strip() for value in values if str(value).strip()]
        else:
            text = str(values).strip()
            cleaned = [text] if text else []
        if cleaned:
            normalized_filters[dim] = cleaned
    sampling = raw.get("sampling") if isinstance(raw.get("sampling"), dict) else {}
    stratify = sampling.get("fields") or []
    if not isinstance(stratify, list):
        stratify = []
    per_group = sampling.get("perCell")
    sample_size = sampling.get("sampleSize")
    return {
        "dimensionFilters": normalized_filters,
        "sampling": {
            "mode": str(sampling.get("mode") or "random"),
            "fields": [str(field).strip() for field in stratify if str(field).strip()],
            "allocation": sampling.get("allocation"),
            "perCell": per_group if isinstance(per_group, int) else None,
            "sampleSize": sample_size if isinstance(sample_size, int) else None,
        },
    }


def _parse_overlays(raw: list[str]) -> list[dict[str, object]]:
    overlay: list[dict[str, object]] = []
    for item in raw:
        try:
            overlay.append(parse_overlay_cli(item))
        except ValueError as exc:
            raise SystemExit(f"--overlay {item!r}: {exc}") from exc
    try:
        return normalize_overlay_dimensions(overlay)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc


def _parse_filters(raw: list[str]) -> dict[str, list[str]]:
    filters: dict[str, list[str]] = {}
    for item in raw:
        try:
            dim_id, values = parse_filter_cli(item)
        except ValueError as exc:
            raise SystemExit(f"--filter {item!r}: {exc}") from exc
        filters[dim_id] = values
    return filters


def _stamp_overlay(
    personas: list[dict],
    overlay: list[dict[str, object]],
    overlay_filters: dict[str, list[str]],
    *,
    seed: int,
) -> None:
    if not overlay:
        return
    stamp_overlay_independent(personas, overlay, overlay_filters, seed=seed + 1)
    rng = random.Random(seed + 2)
    for row in overlay:
        values = overlay_filters.get(str(row["id"])) or list(row["values"])
        if not values:
            continue
        dim_id = str(row["id"])
        for entry in personas:
            dims = entry.setdefault("dimensions", {})
            if dim_id not in dims:
                dims[dim_id] = rng.choice(values)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--count",
        type=int,
        default=None,
        help=(
            f"How many personas to sample (default: {GENERATE_COUNT_DEFAULT}; "
            f"max {GENERATE_COUNT_MAX}; unused when --per-cell / --sample-size / "
            "--strategy fills cells)"
        ),
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help=(
            "Output directory (default: "
            f"persona/datasets/{DEFAULT_POOL_PREFIX}-<count>, listed in "
            "the Playground Dataset picker)"
        ),
    )
    parser.add_argument("--smoke-id", default="0042")
    parser.add_argument(
        "--overlay",
        action="append",
        default=[],
        metavar="SPEC",
        help="Custom dimension: id[:label]=value,value (repeatable)",
    )
    parser.add_argument(
        "--filter",
        action="append",
        default=[],
        metavar="SPEC",
        help="Constrain a schema or overlay dimension: id=value,value (repeatable)",
    )
    parser.add_argument(
        "--stratify",
        action="append",
        default=[],
        metavar="FIELD",
        help="Grid axes for --per-cell / --sample-size (default: every --filter id)",
    )
    parser.add_argument(
        "--allocation",
        choices=("perCell", "equalTotal", "proportional", "independentMarginal"),
        default=None,
        help="Stratified allocation (default: perCell if --per-cell, else independentMarginal if --sample-size)",
    )
    parser.add_argument(
        "--per-cell",
        type=int,
        default=None,
        help="Rows per filter cell (Playground per-cell). Also required with --task.",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=None,
        help="Total rows across cells (Playground total / equalTotal / proportional)",
    )
    parser.add_argument(
        "--task",
        default=None,
        help="Fill grounding probe cells for this task (requires --per-cell)",
    )
    parser.add_argument(
        "--strategy",
        default=None,
        metavar="PATH",
        help=(
            "Fill this task's stratified cells from persona_strategy.json. Writes "
            f"persona/datasets/{DEFAULT_POOL_PREFIX}-strategy-<task>/ "
            "(listed in the Playground Dataset picker)."
        ),
    )
    args = parser.parse_args()

    if args.task and args.strategy:
        raise SystemExit("Use either --task (grounding) or --strategy, not both")
    if args.count is not None and (args.count < 1 or args.count > GENERATE_COUNT_MAX):
        raise SystemExit(f"--count must be 1..{GENERATE_COUNT_MAX}")
    if args.per_cell is not None and args.per_cell < 1:
        raise SystemExit("--per-cell must be >= 1")
    if args.sample_size is not None and args.sample_size < 1:
        raise SystemExit("--sample-size must be >= 1")

    overlay = _parse_overlays(args.overlay)
    cli_filters = _parse_filters(args.filter)
    overlay_ids = {str(row["id"]) for row in overlay}
    remapped: dict[str, list[str]] = {}
    for key, values in cli_filters.items():
        slug = key.strip().lower().replace("-", "_")
        remapped[slug if slug in overlay_ids else key] = values
    cli_filters = remapped
    overlay_filters = fill_overlay_filters(overlay, cli_filters) if overlay else {}

    strategy_path: Path | None = None
    strategy_meta: dict[str, object] | None = None
    grounding_meta: dict[str, object] | None = None
    stratum_top_up: list[dict[str, str]] | None = None
    filters = dict(cli_filters)
    fields = [
        str(field).removeprefix("dimensions.").strip()
        for field in args.stratify
        if str(field).strip()
    ]
    allocation = args.allocation
    per_cell = args.per_cell
    sample_size = args.sample_size
    count = args.count

    if args.strategy:
        strategy_path = _resolve_strategy_path(args.strategy)
        strategy = _load_strategy(strategy_path)
        strategy_filters = strategy.get("dimensionFilters")
        if not isinstance(strategy_filters, dict) or not strategy_filters:
            raise SystemExit(f"{strategy_path} has no dimensionFilters")
        filters = {str(key): list(values) for key, values in strategy_filters.items()}
        filters.update(cli_filters)
        sampling = strategy.get("sampling") if isinstance(strategy.get("sampling"), dict) else {}
        if not fields:
            fields = [
                str(field).removeprefix("dimensions.").strip()
                for field in (sampling.get("fields") or [])
                if str(field).strip()
            ]
        if allocation is None:
            allocation = str(sampling.get("allocation") or "").strip() or None
        if per_cell is None and isinstance(sampling.get("perCell"), int):
            per_cell = sampling.get("perCell")
        if sample_size is None and isinstance(sampling.get("sampleSize"), int):
            sample_size = sampling.get("sampleSize")
        strategy_meta = {
            "strategy_path": str(strategy_path.relative_to(REPO_ROOT)),
            "dimensionFilters": filters,
            "sampling": {
                "mode": sampling.get("mode"),
                "fields": fields,
                "allocation": allocation,
                "perCell": per_cell,
                "sampleSize": sample_size,
            },
        }
    elif args.task:
        if per_cell is None:
            raise SystemExit("--task requires --per-cell >= 1")
        stratum_top_up, grounding_meta = _stratum_top_up_from_task(args.task)
        count = GENERATE_COUNT_DEFAULT if count is None else count
    else:
        if allocation is None:
            if per_cell is not None:
                allocation = "perCell"
            elif sample_size is not None:
                allocation = "independentMarginal"
        if not fields and (per_cell is not None or sample_size is not None):
            fields = list(filters)

    if args.out is not None:
        out = args.out if args.out.is_absolute() else REPO_ROOT / args.out
    elif strategy_path is not None:
        out = _strategy_out_dir(_slug(strategy_path.parent.name))
    else:
        out = _default_out_dir(count if count and count > 0 else GENERATE_COUNT_DEFAULT)

    _progress(
        "prepare",
        f"Output → {out.relative_to(REPO_ROOT) if out.is_relative_to(REPO_ROOT) else out}",
    )
    removed = _wipe_stale_personas(out)
    if removed:
        _progress("prepare", f"Removed {removed} stale persona_*.yaml")

    if args.task:
        _progress(
            "sample",
            f"Sampling grounding cells ({len(stratum_top_up or [])} × {per_cell})…",
        )
        personas = generate_persona_pool(
            count=count or 0,
            seed=args.seed,
            smoke_persona_id=args.smoke_id,
            stratum_top_up=stratum_top_up,
            min_per_stratum=per_cell or 0,
            extra_filters={
                key: list(values)
                for key, values in filters.items()
                if key not in overlay_ids
            }
            or None,
            include_smoke=(count or 0) > 0,
        )
        _stamp_overlay(personas, overlay, overlay_filters, seed=args.seed)
        folder_count = count or 0
    else:
        _progress("sample", "Sampling Full DAG…")
        try:
            generated = generate_synthetic_personas(
                count=count,
                seed=args.seed,
                dimension_filters=filters or None,
                stratify_fields=fields or None,
                allocation=allocation,
                per_cell=per_cell,
                sample_size=sample_size,
                overlay_dimensions=overlay or None,
                catalog_path=REPO_ROOT / "persona/schema/dimensions.json",
                force_pin=strategy_path is not None,
            )
        except ValueError as exc:
            raise SystemExit(str(exc)) from exc
        personas = generated.personas
        overlay = generated.overlay
        folder_count = generated.folder_count

    if not personas:
        raise SystemExit("generation produced no personas")
    _progress("sample", f"Sampled {len(personas)} personas")

    kind = (
        f"{DEFAULT_POOL_PREFIX}-strategy-{_slug(strategy_path.parent.name)}"
        if strategy_path is not None
        else f"{DEFAULT_POOL_PREFIX}-{folder_count if folder_count > 0 else len(personas)}"
    )
    _progress("write", f"Writing {len(personas)} YAML files…")
    manifest = write_persona_dataset(
        out_dir=out,
        personas=personas,
        repo_root=REPO_ROOT,
        kind=kind,
        seed=args.seed,
        smoke_persona_id=args.smoke_id,
        overlay_dimensions=overlay or None,
        on_progress=_write_progress,
    )
    if strategy_meta is not None:
        manifest["stratum_top_up"] = {
            "strategy": strategy_meta,
            "count": len(personas),
        }
        (out / "manifest.json").write_text(
            json.dumps(manifest, indent=2) + "\n",
            encoding="utf-8",
        )
    if grounding_meta is not None:
        manifest["stratum_top_up"] = {
            "task": args.task,
            "min_per_stratum": per_cell,
            "strata_count": len(stratum_top_up or []),
            "grounding": grounding_meta,
        }
        (out / "manifest.json").write_text(
            json.dumps(manifest, indent=2) + "\n",
            encoding="utf-8",
        )

    rel_out = out.relative_to(REPO_ROOT) if out.is_relative_to(REPO_ROOT) else out
    _progress("done", f"Wrote {manifest['count']} personas to {rel_out}")
    if folder_count > 0:
        print(f"Smoke: persona_{manifest['smoke_persona_id']}.yaml")
    print(
        f"Dimensions: {manifest.get('dimension_count', len(manifest['dimension_ids']))} fields"
    )
    if overlay:
        print(
            "Custom dimensions: "
            + ", ".join(f"{row['id']} ({row['label']})" for row in overlay)
        )
    if _is_picker_listed(out):
        print(f"Playground Dataset picker: {rel_out}")
    else:
        print(
            "Not listed in the Playground Dataset picker "
            f"(use --out persona/datasets/{DEFAULT_POOL_PREFIX}-<name>)."
        )
    if grounding_meta is not None:
        print(
            f"Filled {len(stratum_top_up or [])} grounding cells × {per_cell} "
            f"from {args.task}"
        )
    if strategy_path is not None:
        print(f"Filled strategy cells from {strategy_path.relative_to(REPO_ROOT)}")
        print(f'Point the task "pool" at "{rel_out}", or pick it in Playground Dataset.')


if __name__ == "__main__":
    main()
