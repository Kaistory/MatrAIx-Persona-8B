# Trải nghiệm Vita Soul Studio & Cá tính Giọng nói (VinFast VF9)

Truy cập địa chỉ: `https://192.168.137.242:5173/` (hoặc `http://localhost:5173/` / `http://172.20.10.6:5173/`)
- **Xác thực SSL**: Do hệ thống sử dụng chứng chỉ HTTPS nội bộ cho môi trường dev, nếu trình duyệt cảnh báo *"Kết nối không riêng tư"* (*Your connection is not private*), hãy chọn **Nâng cao (Advanced)** ➡️ **Tiếp tục truy cập (Proceed)**.
- **Đăng nhập**: Nếu xuất hiện màn hình yêu cầu mật khẩu bảo vệ, hãy nhập `dev` rồi bấm **"Đăng nhập"** (hoặc "Login") để vào hệ thống.
- **Điều hướng không gian**:
  1. **Trên buồng lái Cockpit (Màn hình trung tâm VF9)**: Nhấn vào biểu tượng **Kho ứng dụng** (App Launcher) ở thanh điều khiển dọc bên trái, sau đó chọn ứng dụng **"Vita Soul"** (biểu tượng ✨) để mở giao diện quản lý và kích hoạt nhanh hồ sơ cá tính giọng nói.
  2. **Trên không gian Vita Soul Studio**: Chọn tab **"Vita Soul"** trên thanh điều hướng chính để mở bảng thiết kế cá tính, xem chi tiết Soul Core, danh mục profile, hội thoại mẫu và trình tạo profile mới.

---

### Nhiệm vụ của bạn:

1. **Khám phá Vita Soul Core & Thứ tự ưu tiên an toàn**:
   - **Soul Core (`SOUL.md`)**: Tìm hiểu bản sắc cốt lõi không thể thỏa hiệp của Vita: Trợ lý ô tô thông minh, luôn ưu tiên an toàn của người lái, giao tiếp tiếng Việt tự nhiên, tôn trọng người dùng và không bịa đặt dữ liệu xe.
   - **Quy tắc ưu tiên kiến trúc**: Quan sát nguyên tắc vận hành:
     $$\text{Safety Gate / Trạng thái xe / Tool result} \longrightarrow \text{Rulebook \& AGENT} \longrightarrow \text{Vita Soul (SOUL.md)} \longrightarrow \text{Profile biểu đạt} \longrightarrow \text{TTS}$$
     *Lưu ý: Profile và Persona không bao giờ có thể ghi đè giới hạn an toàn khi xe đang di chuyển.*

2. **Duyệt & Kích hoạt 7 Profile Biểu đạt Vita Soul**:
   Thử nghiệm chuyển đổi qua toàn bộ 7 hồ sơ biểu đạt trong catalog:
   - `Normal` (Chuẩn mực): Chuyên nghiệp, trung tính, trực tiếp, tập trung xử lý tác vụ (Voice Zara).
   - `Sweet` (Ngọt ngào): Giọng dịu dàng, ấm áp, thủ thỉ, ân cần (Voice Freya).
   - `Chao` (Thân thiện): Xưng hô "mình - bạn", lời chào đặc trưng *"Xin chào, lại là Chao đây"* (Voice Chao).
   - `Cheeky` (Hóm hỉnh): Tinh nghịch, lém lỉnh có chừng mực, xưng hô thân mật khi được chọn, tự động chuyển về nghiêm túc khi có nguy cơ an toàn hoặc có hành khách (Voice Adam).
   - `Tươi sáng` (Rạng rỡ): Nhanh, linh hoạt, giàu năng lượng tích cực (Voice Mai).
   - `Mộc mạc` (Chân chất): Tự nhiên, gần gũi, chân thành như người bạn đồng hành (Voice My).
   - `Điềm tĩnh` (Thư thái): Vững vàng, chừng mực, giọng trầm ấm, độ tin cậy cao (Voice Hien).

3. **Trải nghiệm Chi tiết Profile & Giọng đọc ElevenLabs TTS**:
   - Bấm chọn từng profile để xem chi tiết: Thông tin giọng đọc ElevenLabs TTS, nguyên tắc biểu đạt (prompt hướng dẫn) và các cặp ví dụ hội thoại thực tế (ví dụ: điều chỉnh điều hòa, từ chối mở cốp khi xe đang chạy).
   - Quan sát trạng thái kích hoạt `ĐANG DÙNG` / `Đang áp dụng`.

4. **Khám phá Trình tạo Profile Local (Profile Authoring)**:
   - Xem bảng tạo profile mới: Đặt tên, ID kỹ thuật, mô tả cảm nhận, gán giọng ElevenLabs tiếng Việt, nhập nguyên tắc tính cách và cặp câu thoại mẫu.

5. **Lưu đánh giá**:
   Sau khi hoàn tất trải nghiệm, hãy đóng vai Persona của bạn để lưu kết quả đánh giá vào file `/app/output/soul_studio_experience.json`:

```json
{
  "decision_subject_id": "vita_soul_studio",
  "decision_subject_label": "Vita Soul Studio & Voice Persona",
  "decision_outcome": "selected",
  "basis_primary": "<convenience|features|quality|taste|trust|familiarity|novelty|fit|other>",
  "exploration_style": "<quick_pick|compared_multiple|deep_research|hesitant>",
  "reason": "<Cảm nhận chi tiết của bạn về giao diện Vita Soul Studio, các profile biểu đạt giọng nói tiếng Việt, tính tự nhiên của ElevenLabs TTS, sự an toàn của Soul Core và mức độ cá nhân hóa>",
  "task_favorite_feature": "<profile_switching|sample_dialogues|tts_voice_preview|soul_core_viewer|custom_profile_creator|cockpit_stage_integration>",
  "task_favorite_profile": "<normal|sweet|chao|cheeky|bright|rustic|calm|custom>",
  "task_ease_of_use_rating": 5
}
```

Bạn cũng có thể lưu file tự đánh giá người dùng tại `/app/output/user_feedback.json`:
```json
{
  "overallExperienceRating": 9,
  "satisfactionBucket": "yes",
  "personaFeedbackSummary": "<Nhận xét tổng quan về trải nghiệm Soul Studio>"
}
```

---

**Yêu cầu các trường:**
- `decision_subject_id`: Mã đối tượng đánh giá (`"vita_soul_studio"`).
- `decision_subject_label`: Tên hiển thị (`"Vita Soul Studio & Voice Persona"`).
- `decision_outcome`: Quyết định của bạn (`selected`, `considered`, `rejected`, `deferred`, `skipped`).
- `basis_primary`: Yếu tố chính chi phối đánh giá (`quality`, `taste`, `features`, `novelty`, `fit`, `convenience`, `trust`, `familiarity`, `other`).
- `exploration_style`: Phong cách khám phá (`quick_pick`, `compared_multiple`, `deep_research`, `hesitant`).
- `reason`: Nêu rõ lý do và cảm nhận chi tiết dưới góc nhìn cá tính và nhu cầu của Persona.
- `task_favorite_feature`: Tính năng bạn ấn tượng nhất (`profile_switching`, `sample_dialogues`, `tts_voice_preview`, `soul_core_viewer`, `custom_profile_creator`, `cockpit_stage_integration`).
- `task_favorite_profile`: Profile giọng nói bạn thích nhất (`normal`, `sweet`, `chao`, `cheeky`, `bright`, `rustic`, `calm` hoặc mã profile tự tạo).
- `task_ease_of_use_rating`: Điểm đánh giá độ dễ sử dụng từ 1 đến 5 (số nguyên).
