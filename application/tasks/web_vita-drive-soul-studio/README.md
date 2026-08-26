# Web Task: Vita Soul Studio & Voice Persona (TTS Voice Exploration & Personality Tuning)

Mô phỏng trải nghiệm người dùng đối với bảng thiết kế và tinh chỉnh cá tính giọng nói **Vita Soul Studio** (khám phá 6 profile biểu đạt giọng nói, nghe thử ElevenLabs TTS tiếng Việt, tinh chỉnh thông số giọng đọc và hội thoại mẫu) trên trình duyệt web.

## Suggested setup (non-binding)

- **Agent driver:** `persona-browser-use` (hoặc `persona-openhands-sdk`)
- **Website URL:** `http://172.17.0.1:5173/` (chọn tab **"Vita Soul"**)
- **Local repo:** `/home/khaidq9/Documents/GitHub/vita-drive-assistant-lab`
- **Output:** `/app/output/soul_studio_experience.json` và `/app/output/user_feedback.json`

## Khởi động toàn bộ stack trước khi chạy test

```bash
cd /home/khaidq9/Documents/GitHub/vita-drive-assistant-lab
npm run dev
```

- Web Frontend: `http://localhost:5173` (hoặc `http://172.17.0.1:5173`) (mật khẩu: `dev`)
- Backend API: `http://localhost:3001`
- Python Agent: `http://localhost:8787`

## Chạy kiểm thử mẫu qua CLI

```bash
uv run matraix run \
  -a persona-browser-use \
  -m anthropic/claude-haiku-4-5 \
  --ak persona_path=persona/datasets/matraix-persona-dev-sample/persona_0042.yaml \
  -p application/tasks/web_vita-drive-soul-studio
```
