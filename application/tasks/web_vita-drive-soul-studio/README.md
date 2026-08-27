# Web Task: Vita Soul Studio & Voice Persona (TTS Voice Exploration & Personality Tuning)

Đánh giá trải nghiệm người dùng (Persona) đối với không gian thiết kế và tinh chỉnh cá tính giọng nói **Vita Soul Studio** (khám phá bản sắc Soul Core, duyệt & kích hoạt 7 profile biểu đạt tiếng Việt, nghe thử ElevenLabs TTS, kiểm tra an toàn theo ngữ cảnh lái xe và tạo profile local) trên nền tảng trợ lý xe hơi VinFast VF9.

---

## 1. Mục tiêu & Bối cảnh

Task này mô phỏng hành vi của người dùng / chủ xe khi khám phá và cá nhân hóa giọng nói của trợ lý Vita trong buồng lái thông minh:
- **Thứ tự ưu tiên an toàn**: Đảm bảo hiểu rõ nguyên tắc `Safety Gate / State xe / Tool result → Rulebook & AGENT → Vita Soul (SOUL.md) → Profile biểu đạt → TTS`. Profile và tính cách không bao giờ được phép ghi đè an toàn xe.
- **7 Profile Biểu đạt**: Thử nghiệm chuyển đổi qua các profile: `normal` (Chuẩn mực), `sweet` (Ngọt ngào), `chao` (Thân thiện), `cheeky` (Hóm hỉnh), `bright` (Tươi sáng), `rustic` (Mộc mạc), `calm` (Điềm tĩnh).
- **Trải nghiệm buồng lái đa bề mặt**: Tương tác qua cả **Vita Soul Stage** trên Cockpit (App Launcher ✨) và giao diện chuyên sâu **Soul Studio Panel**.
- **Đánh giá cá nhân hóa**: Đóng vai Persona để xuất cảm nhận, tính năng yêu thích, profile ưng ý nhất và xếp hạng trải nghiệm.

---

## 2. Cấu trúc thư mục Task

```text
application/tasks/web_vita-drive-soul-studio/
├── task.toml                  # Khai báo cấu hình task, runtime, timeouts, artifacts
├── instruction.md             # Hướng dẫn chi tiết cho browser agent và schema output
├── input/
│   ├── context.md             # Bối cảnh kỹ thuật, kiến trúc phân lớp Vita Soul
│   └── self_report_schema.yaml # Schema tự đánh giá persona (user_feedback.json)
├── tests/
│   ├── test.sh                # Entrypoint cho verifier
│   ├── test_state.py          # Script kiểm chứng artifact và sinh structured_output.json
│   └── verifier_env.sh        # Thiết lập biến môi trường cho verifier
├── reporting.json             # Chính sách phân phối báo cáo theo phân khúc persona
├── persona_strategy.json      # Bộ lọc nhóm đối tượng persona và chiến lược lấy mẫu
├── solution/
│   └── solve.sh               # Oracle script tự động hóa (Playwright) phục vụ smoke test
└── README.md                  # Tài liệu hướng dẫn sử dụng và kiểm thử task
```

---

## 3. Thiết lập môi trường (Suggested Setup)

- **Agent driver khuyến nghị:** `persona-browser-use` (hoặc `persona-openhands-sdk`)
- **Website URL:** `https://192.168.137.242:5173/` (hoặc `http://localhost:5173/` / `http://172.20.10.6:5173/`)
- **Mật khẩu bảo vệ:** `dev`
- **Mã nguồn ứng dụng SUT:** `/home/khaidq9/Documents/GitHub/vita-drive-assistant-lab`
- **Artifacts đầu ra:**
  - `/app/output/soul_studio_experience.json` (bắt buộc)
  - `/app/output/user_feedback.json` (tùy chọn)

### Khởi động toàn bộ stack SUT:

```bash
cd /home/khaidq9/Documents/GitHub/vita-drive-assistant-lab
npm run dev
```

- Web Frontend: `http://localhost:5173` (hoặc `http://172.17.0.1:5173`)
- Backend API: `http://localhost:3001`
- Python Agent: `http://localhost:8787`

---

## 4. Chạy kiểm thử

### Chạy Oracle Smoke Test (không cần API key):

```bash
uv run matraix run \
  -a oracle \
  -p application/tasks/web_vita-drive-soul-studio
```

### Chạy Persona Browser Agent:

```bash
uv run matraix run \
  -a persona-browser-use \
  -m anthropic/claude-haiku-4-5 \
  --ak persona_path=persona/datasets/matraix-persona-dev-sample/persona_0042.yaml \
  -p application/tasks/web_vita-drive-soul-studio
```

### Chạy kiểm thử Verifier độc lập:

```bash
python3 application/tasks/web_vita-drive-soul-studio/tests/test_state.py
```
