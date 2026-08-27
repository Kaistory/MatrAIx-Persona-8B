# Tài liệu Kỹ thuật: Web Task Vita Drive Soul Studio

## 1. Giới thiệu tổng quan

**Vita Drive Soul Studio** (`web_vita-drive-soul-studio`) là web task thuộc module ứng dụng nghiên cứu sản phẩm xe hơi thông minh của MatrAIx, đánh giá trải nghiệm người dùng đối với hệ thống thiết kế và cá nhân hóa giọng nói/tính cách của trợ lý ảo **Vita** trên buồng lái VinFast VF9.

- **Đường dẫn task**: [`application/tasks/web_vita-drive-soul-studio/`](file:///home/khaidq9/Documents/GitHub/MatrAIx-Persona-8B/application/tasks/web_vita-drive-soul-studio)
- **Mã nguồn SUT tham chiếu**: [`vita-drive-assistant-lab`](/home/khaidq9/Documents/GitHub/vita-drive-assistant-lab)
- **Hình thức tương tác**: `web` (trình duyệt web mô phỏng buồng lái xe thông minh)
- **Agent driver mặc định**: `persona-browser-use` (hoặc `persona-openhands-sdk`)
- **Tập tin kết quả**: `/app/output/soul_studio_experience.json` và `/app/output/user_feedback.json`

---

## 2. Kiến trúc Vita Soul & Nguyên tắc vận hành

### Phân lớp ưu tiên
Hệ thống vận hành theo chuỗi ưu tiên an toàn nghiêm ngặt:
$$\text{Safety Gate / Trạng thái xe / Tool result} \longrightarrow \text{Rulebook \& AGENT} \longrightarrow \text{Vita Soul (SOUL.md)} \longrightarrow \text{Profile biểu đạt} \longrightarrow \text{TTS}$$

1. **Safety & Tool Gate**: Rào chắn an toàn khi xe di chuyển, kết quả truy vấn telemetry xe luôn có quyền phủ quyết cao nhất.
2. **Soul Core (`SOUL.md`)**: Lõi danh tính ổn định của Vita (trung thực, an toàn, tôn trọng, giao tiếp tiếng Việt tự nhiên).
3. **Profile biểu đạt (`configs/vita-soul/profiles/`)**: 7 profile cá tính thay đổi phong thái và giọng đọc nhưng không thay đổi sự thật hay vượt rào an toàn:
   - `normal` (Chuẩn mực) - Zara TTS (`QocxxnxEa0x8mrL2d4VT`)
   - `sweet` (Ngọt ngào) - Freya TTS (`rXOGzMiqbmjugMpzKMEx`)
   - `chao` (Thân thiện) - Chao TTS (`rXOGzMiqbmjugMpzKMEx`)
   - `cheeky` (Hóm hỉnh) - Adam TTS (`pNInz6obpgDQGcFmaJgB`)
   - `bright` (Tươi sáng) - Mai TTS (`d5HVupAWCwe4e6GvMCAL`)
   - `rustic` (Mộc mạc) - My TTS (`RmcV9cAq1TByxNSgbii7`)
   - `calm` (Điềm tĩnh) - Hien TTS (`jdlxsPOZOHdGEfcItXVu`)
4. **Local Profile Authoring**: Tính năng cho phép tạo hồ sơ biểu đạt cục bộ mới với prompt cá nhân hóa và giọng ElevenLabs riêng.

---

## 3. Các bề mặt tương tác trên giao diện

1. **Cockpit Stage (`SoulStage`)**:
   - Truy cập từ **App Launcher** (Kho ứng dụng ✨) trên màn hình trung tâm xe VF9.
   - Thẻ hiển thị các profile trực quan, nhãn trạng thái `ĐANG DÙNG`.
   - Kích hoạt profile nhanh với phản hồi thời gian thực.
2. **Studio View (`SoulStudioPanel`)**:
   - Truy cập từ tab **"Vita Soul"** trên menu chính.
   - Hiển thị chi tiết `SOUL.md`, thống kê ngân sách ký tự runtime.
   - Xem chi tiết từng profile: prompt nguyên tắc, ví dụ đối thoại, voice TTS tags.
   - Biểu mẫu tạo profile mới.

---

## 4. Hướng dẫn chạy và kiểm thử

### Khởi động hệ thống SUT
```bash
cd /home/khaidq9/Documents/GitHub/vita-drive-assistant-lab
npm run dev
```

### Chạy Oracle Smoke Test
```bash
uv run matraix run \
  -a oracle \
  -p application/tasks/web_vita-drive-soul-studio
```

### Chạy Persona Browser Agent
```bash
uv run matraix run \
  -a persona-browser-use \
  -m anthropic/claude-haiku-4-5 \
  --ak persona_path=persona/datasets/matraix-persona-dev-sample/persona_0042.yaml \
  -p application/tasks/web_vita-drive-soul-studio
```

### Chạy kiểm thử Verifier
```bash
python3 application/tasks/web_vita-drive-soul-studio/tests/test_state.py
```
