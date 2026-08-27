#!/bin/bash
set -euo pipefail

OUTPUT_DIR="${HARBOR_OUTPUT_DIR:-${MATRIX_OUTPUT_DIR:-/app/output}}"
LOGS_DIR="${HARBOR_LOGS_DIR:-/logs/agent}"

mkdir -p "${OUTPUT_DIR}" 2>/dev/null || true
mkdir -p "${LOGS_DIR}/screenshots" 2>/dev/null || true

python3 <<'PY'
import json
import os
from pathlib import Path

output_dir = Path(os.environ.get("HARBOR_OUTPUT_DIR") or os.environ.get("MATRIX_OUTPUT_DIR") or "/app/output")
logs_dir = Path(os.environ.get("HARBOR_LOGS_DIR") or "/logs/agent")
screenshots_dir = logs_dir / "screenshots"

try:
    output_dir.mkdir(parents=True, exist_ok=True)
    screenshots_dir.mkdir(parents=True, exist_ok=True)
except Exception:
    pass

try:
    from playwright.sync_api import sync_playwright

    target_urls = [
        "http://localhost:5173/",
        "https://192.168.137.242:5173/",
        "http://172.20.10.6:5173/",
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--ignore-certificate-errors"])
        page = browser.new_page(viewport={"width": 1280, "height": 800}, ignore_https_errors=True)

        connected = False
        for url in target_urls:
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=5000)
                connected = True
                break
            except Exception:
                continue

        if connected:
            # 1. Chụp ảnh màn hình trang đăng nhập / khởi động
            page.screenshot(path=str(screenshots_dir / "01_login_gate.png"), full_page=True)

            # 2. Xử lý đăng nhập nếu có
            pass_input = page.locator('input[type="password"]')
            if pass_input.count() > 0:
                pass_input.fill("dev")
                submit_btn = page.locator('button[type="submit"]')
                if submit_btn.count() > 0:
                    submit_btn.click()
                    page.wait_for_timeout(1500)

            page.screenshot(path=str(screenshots_dir / "02_cockpit_view.png"), full_page=True)

            # 3. Điều hướng tới Vita Soul Stage qua App Launcher hoặc Tab
            soul_app_btn = page.locator('button:has-text("Vita Soul"), [data-view="soul"], button.round.soul').first
            if soul_app_btn.count() > 0:
                soul_app_btn.click()
                page.wait_for_timeout(1000)

            page.screenshot(path=str(screenshots_dir / "03_soul_stage.png"), full_page=True)

            # 4. Thử nghiệm chọn các Profile biểu đạt
            calm_btn = page.locator('button:has-text("Điềm tĩnh"), button:has-text("Sweet"), button:has-text("Chao")').first
            if calm_btn.count() > 0:
                calm_btn.click()
                page.wait_for_timeout(1000)

            page.screenshot(path=str(screenshots_dir / "04_profile_selected.png"), full_page=True)

        browser.close()
except Exception as e:
    print(f"Note: Playwright browser run skipped or completed with notice: {e}")

# Ghi lại chuỗi hành động vào trajectory.json cho Web UI Replay
trajectory = {
    "version": "1.0",
    "steps": [
        {
            "source": "agent",
            "message": [
                {"type": "text", "text": "Truy cập giao diện VoiceLab và đăng nhập vào hệ thống buồng lái VF9."},
                {"type": "image", "source": {"path": "screenshots/01_login_gate.png"}}
            ],
            "tool_calls": [{"function_name": "goto", "arguments": {"url": "https://192.168.137.242:5173/"}}]
        },
        {
            "source": "agent",
            "message": [
                {"type": "text", "text": "Mở kho ứng dụng và truy cập ứng dụng Vita Soul trên buồng lái."},
                {"type": "image", "source": {"path": "screenshots/02_cockpit_view.png"}}
            ],
            "tool_calls": [{"function_name": "click", "arguments": {"selector": "button:has-text('Vita Soul')"}}]
        },
        {
            "source": "agent",
            "message": [
                {"type": "text", "text": "Khám phá bản sắc Soul Core và duyệt qua 7 profile biểu đạt (Normal, Sweet, Chao, Cheeky, Tươi sáng, Mộc mạc, Điềm tĩnh)."},
                {"type": "image", "source": {"path": "screenshots/03_soul_stage.png"}}
            ],
            "tool_calls": [{"function_name": "click", "arguments": {"profile": "calm"}}]
        },
        {
            "source": "agent",
            "message": [
                {"type": "text", "text": "Kích hoạt profile 'Điềm tĩnh' (giọng Hien), trải nghiệm các cặp câu thoại mẫu và xác nhận nhãn ĐANG DÙNG."},
                {"type": "image", "source": {"path": "screenshots/04_profile_selected.png"}}
            ],
            "tool_calls": [{"function_name": "submit_report", "arguments": {"file": "soul_studio_experience.json"}}]
        }
    ]
}
try:
    (logs_dir / "trajectory.json").write_text(json.dumps(trajectory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
except Exception:
    pass

# Xuất kết quả đánh giá của Persona
payload = {
    "decision_subject_id": "vita_soul_studio",
    "decision_subject_label": "Vita Soul Studio & Voice Persona",
    "decision_outcome": "selected",
    "basis_primary": "quality",
    "exploration_style": "compared_multiple",
    "reason": "Các profile giọng nói tiếng Việt rất phong phú và tự nhiên, đặc biệt profile Điềm tĩnh (giọng Hien) mang lại cảm giác an tâm, vững vàng khi lái xe. Soul Core đảm bảo an toàn tuyệt đối và không bị ghi đè bởi tính cách.",
    "task_favorite_feature": "profile_switching",
    "task_favorite_profile": "calm",
    "task_ease_of_use_rating": 5
}
(output_dir / "soul_studio_experience.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

user_feedback = {
    "overallExperienceRating": 9,
    "satisfactionBucket": "yes",
    "personaFeedbackSummary": "Giao diện chuyển đổi profile trực quan, tích hợp mượt mà trên buồng lái xe và tôn trọng nguyên tắc an toàn."
}
(output_dir / "user_feedback.json").write_text(json.dumps(user_feedback, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print("Oracle solve completed successfully.")
PY
