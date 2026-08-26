#!/bin/bash
set -euo pipefail

mkdir -p /app/output

python <<'PY'
import json
from pathlib import Path

output = Path("/app/output/dashboard_experience.json")

payload = {
    "decision_subject_id": "vita_car_dashboard",
    "decision_subject_label": "Vita Drive Assistant Dashboard",
    "decision_outcome": "selected",
    "basis_primary": "convenience",
    "exploration_style": "compared_multiple",
    "reason": "Giao diện bảng điều khiển xe trực quan, các nút chỉnh điều hòa và bản đồ dẫn đường dễ nhìn khi lái xe.",
    "task_favorite_feature": "climate_control",
    "task_ease_of_use_rating": 5
}
output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
PY
