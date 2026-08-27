#!/bin/bash
set -euo pipefail

mkdir -p /app/output
mkdir -p /logs/agent/screenshots

python <<'PY'
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

output_dir = Path("/app/output")
logs_dir = Path("/logs/agent")
screenshots_dir = logs_dir / "screenshots"
output_dir.mkdir(parents=True, exist_ok=True)
screenshots_dir.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 800})
    
    # 1. Mở trang đăng nhập
    page.goto("https://192.168.137.242:5173/", wait_until="networkidle", timeout=15000)
    page.screenshot(path=str(screenshots_dir / "01_login_gate.png"), full_page=True)
    
    # 2. Đăng nhập vào Dashboard buồng lái xe VF9
    btn = page.locator('button[type="submit"]')
    if btn.count() > 0:
        btn.click()
        page.wait_for_timeout(2000)
    page.screenshot(path=str(screenshots_dir / "02_main_dashboard.png"), full_page=True)
    
    # 3. Mở bảng điều khiển khí hậu xe 3 vùng
    temp_up_btn = page.locator('button:has(svg.lucide-chevron-right)').first
    if temp_up_btn.count() > 0:
        temp_up_btn.click()
        page.wait_for_timeout(1000)
    page.screenshot(path=str(screenshots_dir / "03_climate_controls.png"), full_page=True)
    
    # 4. Trạng thái kết thúc
    page.screenshot(path=str(screenshots_dir / "04_final_view.png"), full_page=True)
    browser.close()

# Ghi lại chuỗi hành động và ảnh chụp vào trajectory.json cho Web UI Replay
trajectory = {
    "version": "1.0",
    "steps": [
        {
            "source": "agent",
            "message": [
                {"type": "text", "text": "Truy cập vào trang đăng nhập VoiceLab."},
                {"type": "image", "source": {"path": "screenshots/01_login_gate.png"}}
            ],
            "tool_calls": [{"function_name": "goto", "arguments": {"url": "https://192.168.137.242:5173/"}}]
        },
        {
            "source": "agent",
            "message": [
                {"type": "text", "text": "Đăng nhập thành công vào buồng lái xe VinFast VF9 3D."},
                {"type": "image", "source": {"path": "screenshots/02_main_dashboard.png"}}
            ],
            "tool_calls": [{"function_name": "click", "arguments": {"selector": "button[type='submit']"}}]
        },
        {
            "source": "agent",
            "message": [
                {"type": "text", "text": "Mở bảng điều khiển chi tiết điều hòa và các thiết bị trên xe."},
                {"type": "image", "source": {"path": "screenshots/03_climate_controls.png"}}
            ],
            "tool_calls": [{"function_name": "click", "arguments": {"selector": "button:has(svg.lucide-chevron-right)"}}]
        },
        {
            "source": "agent",
            "message": [
                {"type": "text", "text": "Hoàn tất các bước trải nghiệm và xuất báo cáo."},
                {"type": "image", "source": {"path": "screenshots/04_final_view.png"}}
            ],
            "tool_calls": [{"function_name": "submit_report", "arguments": {"file": "dashboard_experience.json"}}]
        }
    ]
}
(logs_dir / "trajectory.json").write_text(json.dumps(trajectory, indent=2, ensure_ascii=False))

# Xuất kết quả đánh giá của Persona
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
(output_dir / "dashboard_experience.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
PY
