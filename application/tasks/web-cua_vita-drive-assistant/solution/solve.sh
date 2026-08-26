#!/usr/bin/env bash
set -euo pipefail

mkdir -p /app/output

cat > /app/output/dashboard_experience.json <<'EOF'
{
  "decision_subject_id": "vita_car_dashboard",
  "decision_subject_label": "Vita Drive Assistant Dashboard",
  "decision_outcome": "selected",
  "basis_primary": "convenience",
  "exploration_style": "compared_multiple",
  "reason": "Giao diện buồng lái VinFast VF9 trực quan, hệ thống điều hòa 3 vùng và phím tắt điều khiển các cửa xe dễ thao tác trên màn hình.",
  "task_favorite_feature": "climate_control_3zone",
  "task_ease_of_use_rating": 5
}
EOF
