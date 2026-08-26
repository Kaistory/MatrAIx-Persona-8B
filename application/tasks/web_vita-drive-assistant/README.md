# Web Task: Vita Drive Assistant Lab

Mô phỏng trải nghiệm người dùng đối với bảng điều khiển xe thông minh **Vita Drive Assistant Lab** chạy local trên trình duyệt.

## Suggested setup (non-binding)

- **Agent driver:** `persona-browser-use` (hoặc `persona-openhands-sdk`)
- **Website URL:** `http://172.17.0.1:5173/` (Localhost từ máy host vào Docker container)
- **Local repo:** `/home/khaidq9/Documents/GitHub/vita-drive-assistant-lab/apps/web`
- **Output:** `/app/output/dashboard_experience.json`

## Khởi động website trước khi chạy test

```bash
cd /home/khaidq9/Documents/GitHub/vita-drive-assistant-lab/apps/web
npm run dev
```

## Chạy kiểm thử mẫu qua CLI

```bash
uv run matraix run \
  -a persona-browser-use \
  -m anthropic/claude-haiku-4-5 \
  --ak persona_path=persona/datasets/matraix-persona-dev-sample/persona_0042.yaml \
  -p application/tasks/web_vita-drive-assistant
```
