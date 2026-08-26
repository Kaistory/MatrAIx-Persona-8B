# Web Task: Vita Scenario Playground & Evaluation Lab (Driving Scenarios & AI Judge)

Mô phỏng trải nghiệm người dùng đối với bảng điều khiển thử nghiệm kịch bản lái xe **Evaluation Playground & Scenario Lab** (chọn tình huống lái xe thực tế, kiểm tra Rule Checklist, kết quả chấm điểm AI Judge, phân luồng Edge/Cloud và xuất dữ liệu QA) trên trình duyệt web.

## Suggested setup (non-binding)

- **Agent driver:** `persona-browser-use` (hoặc `persona-openhands-sdk`)
- **Website URL:** `http://192.168.0.109:8888/` (chọn tab **"Thử nghiệm" / Playground**)
- **Local repo:** `/home/khaidq9/Documents/GitHub/vita-drive-assistant-lab`
- **Output:** `/app/output/playground_experience.json` và `/app/output/user_feedback.json`

## Khởi động toàn bộ stack trước khi chạy test

```bash
cd /home/khaidq9/Documents/GitHub/vita-drive-assistant-lab
bash run-web.sh
# hoặc: npm run dev
```

- Web Frontend: `http://localhost:8888` (mật khẩu: `dev`)
- Backend API: `http://localhost:3001`
- Python Agent: `http://localhost:8787`

## Chạy kiểm thử mẫu qua CLI

```bash
uv run matraix run \
  -a persona-browser-use \
  -m anthropic/claude-haiku-4-5 \
  --ak persona_path=persona/datasets/matraix-persona-dev-sample/persona_0042.yaml \
  -p application/tasks/web_vita-drive-scenario-playground
```
