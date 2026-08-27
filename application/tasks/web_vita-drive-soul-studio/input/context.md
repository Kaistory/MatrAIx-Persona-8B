# Bối cảnh Kỹ thuật: Vita Soul Studio & Cá tính Giọng nói (VinFast VF9)

Không gian thử nghiệm và thiết kế cá tính giọng nói **Vita Soul Studio** là một phân hệ cốt lõi trong nền tảng trợ lý xe hơi thông minh VoiceLab Drive Assistant Lab tại địa chỉ:
**https://192.168.137.242:5173/** (hoặc `http://localhost:5173/` / `http://172.20.10.6:5173/`).

*(Ghi chú: Nếu gặp cảnh báo SSL do sử dụng chứng chỉ nội bộ, chọn **Nâng cao** ➡️ **Tiếp tục truy cập**. Khi xuất hiện màn hình yêu cầu mật khẩu bảo vệ, nhập `dev` rồi bấm **"Đăng nhập"**).*

---

## 1. Kiến trúc phân lớp Vita Soul & Nguyên tắc an toàn

Theo kiến trúc hệ thống Vita Soul (`docs/vita-soul-architecture.vi.md`), Vita phân tách rõ ràng giữa **Danh tính bất biến (Soul Core)** và **Cách thức thể hiện (Expression Profiles)**:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Trạng thái xe / Giới hạn an toàn / Safety Gate / Tool   │ (Ưu tiên cao nhất)
├─────────────────────────────────────────────────────────────┤
│ 2. Rulebook, Capability Catalog & AGENT Workflow            │
├─────────────────────────────────────────────────────────────┤
│ 3. Vita Soul Core (configs/vita-soul/SOUL.md)               │
├─────────────────────────────────────────────────────────────┤
│ 4. Profile Biểu đạt (configs/vita-soul/profiles/<id>/)      │
├─────────────────────────────────────────────────────────────┤
│ 5. Ngữ cảnh Persona / Người dùng (USER / Session Context)   │
└─────────────────────────────────────────────────────────────┘
```

- **Thứ tự ưu tiên an toàn tuyệt đối**: Kết quả công cụ, rào chắn an toàn khi xe chuyển động (Safety Gate) và dữ liệu trạng thái xe luôn đứng trên Soul và Profile.
- **Không bao giờ bịa đặt**: Profile không được phép khẳng định một hành động chưa chạy, mở rộng quyền hạn chưa cấp hoặc bỏ qua an toàn (ví dụ: yêu cầu mở cốp khi xe đang chạy sẽ luôn bị từ chối dứt khoát).

---

## 2. Vita Soul Core (`SOUL.md`)

- **Bản sắc cố định**: Trợ lý AI thông minh, ưu tiên an toàn, tôn trọng người lái, giao tiếp tiếng Việt tự nhiên và chuẩn mực văn hóa.
- **Quản lý ngân sách ký tự (Runtime Budget)**: File `SOUL.md` được giới hạn độ dài chặt chẽ thông qua `manifest.yaml` để tối ưu token runtime và độ trễ phản hồi khi đàm thoại giọng nói.

---

## 3. Catalog 7 Profile Biểu đạt Vita Soul

Hệ thống cung cấp sẵn 7 hồ sơ biểu đạt chuyên biệt:

1. **Normal (Chuẩn mực)**:
   - *Tính cách*: Chuyên nghiệp, bình tĩnh, trung tính, trực tiếp.
   - *Xưng hô*: "mình" - "bạn".
   - *Giọng ElevenLabs*: Zara (`QocxxnxEa0x8mrL2d4VT`) - giọng miền Trung, ấm, tự nhiên, rõ và trung tính.
2. **Sweet (Ngọt ngào)**:
   - *Tính cách*: Dịu dàng, ấm áp, mềm mại, quan tâm vừa đủ và không sến.
   - *Giọng ElevenLabs*: Freya (`rXOGzMiqbmjugMpzKMEx`) - giọng nữ miền Bắc trẻ, mềm và thủ thỉ.
3. **Chao (Thân thiện)**:
   - *Tính cách*: Thân thiện, gần gũi, xưng "mình" - "bạn".
   - *Đặc trưng*: Câu chào cố định *"Xin chào, lại là Chao đây"*.
   - *Giọng ElevenLabs*: Chao (`rXOGzMiqbmjugMpzKMEx`) - giọng nữ tự nhiên, thân thiện.
4. **Cheeky (Hóm hỉnh)**:
   - *Tính cách*: Tinh nghịch, lém lỉnh, cợt nhả có chừng mực, đáp gọn.
   - *Quy tắc an toàn*: Được phép xưng hô thân mật ("con vợ") chỉ khi người dùng tự chọn profile; tự động tắt và chuyển về "mình/bạn" khi có cảnh báo an toàn, có hành khách hoặc người dùng không thoải mái.
   - *Giọng ElevenLabs*: Adam (`pNInz6obpgDQGcFmaJgB`) - nhịp tự tin, cợt nhả, có lực.
5. **Tươi sáng (Rạng rỡ)**:
   - *Tính cách*: Nhanh, linh hoạt, tỉnh táo, giàu năng lượng tích cực.
   - *Giọng ElevenLabs*: Mai (`d5HVupAWCwe4e6GvMCAL`) - giọng nữ tự nhiên, sáng, rõ và linh hoạt.
6. **Mộc mạc (Chân chất)**:
   - *Tính cách*: Tự nhiên, đời thường, chân thành, dễ gần như người bạn đồng hành.
   - *Giọng ElevenLabs*: My (`RmcV9cAq1TByxNSgbii7`) - giọng nữ ấm, mềm, tự nhiên.
7. **Điềm tĩnh (Thư thái)**:
   - *Tính cách*: Vững, chắc chắn, chừng mực, authority cao, câu trọn ý.
   - *Giọng ElevenLabs*: Hien (`jdlxsPOZOHdGEfcItXVu`) - giọng nữ trầm ấm, rõ chữ và chắc chắn.

---

## 4. Các điểm tương tác chính trên Giao diện Web

1. **Buồng lái Cockpit Stage (`SoulStage`)**:
   - Mở từ App Launcher trên màn hình trung tâm xe VF9.
   - Hiển thị danh sách card profile trực quan kèm voice hint.
   - Kích hoạt profile nhanh theo thời gian thực (hiển thị nhãn `ĐANG DÙNG`).
2. **Bảng điều khiển Studio (`SoulStudioPanel`)**:
   - Xem nội dung lõi `SOUL.md`, số ký tự và các phân mục nguyên tắc.
   - Xem chi tiết prompt hướng dẫn tính cách và cặp câu thoại mẫu của từng profile.
   - Nghe thử ElevenLabs TTS tương ứng với từng profile.
   - Khám phá form tạo hồ sơ cục bộ (Local Profile Authoring).

---

## 5. Xuất kết quả đánh giá Persona

Sau khi hoàn tất hành trình trải nghiệm, ghi kết quả vào `/app/output/soul_studio_experience.json` và `/app/output/user_feedback.json` theo đúng schema quy định trong `instruction.md`.
