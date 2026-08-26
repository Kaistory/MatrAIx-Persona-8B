# Web Cocoa Task: Vita Drive Assistant (VinFast VF9 Cockpit & Controls via CocoaAgent)

Mô phỏng trải nghiệm người dùng đối với bảng điều khiển xe điện thông minh **VinFast VF9 Dashboard & Cockpit** thông qua trình duyệt và giao thức **CocoaAgent** (`persona-cocoa` trên môi trường `shared-web-cocoa`).

## Suggested setup

- **Agent driver:** `persona-cocoa`
- **Environment:** `application/shared-web-cocoa` (AIO Sandbox + CocoaAgent)
- **Website URL:** `http://172.17.0.1:5173/`
- **Output:** `/app/output/dashboard_experience.json` và `/app/output/user_feedback.json`

## Khởi động frontend/backend trước khi chạy test

```bash
cd /home/khaidq9/Documents/GitHub/vita-drive-assistant-lab
npm run dev
```

- Web Frontend: `http://localhost:5173` (hoặc `http://172.17.0.1:5173`) (mật khẩu: `dev`)
- Backend API: `http://localhost:3001`

## Chạy kiểm thử qua CLI với CocoaAgent

```bash
uv run matraix run \
  -a persona-cocoa \
  -m openai/gpt-4o-mini \
  --ak persona_path=persona/datasets/generated-persona-dev-1/persona_0042.yaml \
  -p application/tasks/web-cocoa_vita-drive-assistant
```
