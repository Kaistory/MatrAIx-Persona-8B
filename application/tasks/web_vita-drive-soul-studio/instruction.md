# Trải nghiệm Vita Soul Studio & Cá tính Giọng nói (VinFast VF9)

Truy cập địa chỉ `http://172.17.0.1:5173/`.
- **Đăng nhập**: Nếu xuất hiện màn hình yêu cầu đăng nhập, hãy nhập mật khẩu là `dev` rồi bấm nút **"Đăng nhập"** (hoặc "Login") để vào hệ thống.
- **Điều hướng**: Sau khi vào trong, bấm chuyển sang tab **"Vita Soul"** (hoặc "Soul Studio") trên thanh điều hướng để khám phá không gian thiết kế cá tính giọng nói của trợ lý xe thông minh.

### Nhiệm vụ của bạn:
1. **Khám phá Soul Studio & Hồ sơ biểu đạt**:
   - **Soul Core & Giới thiệu danh tính**: Xem cấu trúc Soul cố định của Vita (ân cần, an toàn, tôn trọng người lái).
   - **Duyệt 6 Profile biểu đạt**: Chuyển đổi và thử nghiệm qua các profile: `Normal` (Chuẩn mực), `Sweet` (Ngọt ngào), `Cheeky` (Hóm hỉnh), `Tươi sáng` (Rạng rỡ), `Mộc mạc` (Chân chất), `Điềm tĩnh` (Thư thái).
   - **Hội thoại mẫu & Nghe thử TTS**: Bấm vào các câu thoại mẫu để nghe thử cách phát âm tiếng Việt tương ứng với từng giọng đọc ElevenLabs (Mai, My, Hien).
   - **Cấu hình giọng đọc (Voice Settings)**: Xem bảng thông số giọng nói, điều chỉnh tốc độ đọc, độ ổn định (Stability) và độ tương đồng (Similarity Boost).
   - **Trải nghiệm tạo Profile mới**: Xem biểu mẫu tạo profile cá nhân hóa (Profile Editor / YAML Preview).

2. **Lưu đánh giá**:
   Sau khi trải nghiệm các tính năng trong Soul Studio, hãy đóng vai Persona của bạn để lưu kết quả đánh giá vào `/app/output/soul_studio_experience.json`:

```json
{
  "decision_subject_id": "vita_soul_studio",
  "decision_subject_label": "Vita Soul Studio & Voice Persona",
  "decision_outcome": "selected",
  "basis_primary": "<convenience|features|quality|taste|trust|familiarity|novelty|fit|other>",
  "exploration_style": "<quick_pick|compared_multiple|deep_research|hesitant>",
  "reason": "<Cảm nhận chi tiết của bạn về giao diện Soul Studio, các profile biểu đạt giọng nói tiếng Việt, tính tự nhiên của ElevenLabs TTS và mức độ cá nhân hóa>",
  "task_favorite_feature": "<tính năng bạn thích nhất, ví dụ: profile_switching, sample_dialogues, tts_voice_preview, voice_tuning_sliders, custom_profile_creator>",
  "task_favorite_profile": "<profile giọng nói bạn thích nhất: normal|sweet|cheeky|bright|rustic|calm>",
  "task_ease_of_use_rating": 5
}
```

Yêu cầu:
- `basis_primary`: Yếu tố chính ảnh hưởng đến đánh giá của bạn (ví dụ: `quality`, `taste`, `features`, `novelty`, `fit`,...).
- `exploration_style`: Phong cách khám phá của bạn (`quick_pick`, `compared_multiple`, `deep_research`, `hesitant`).
- `reason`: Nêu rõ lý do dưới góc nhìn cá nhân (persona) của bạn.
- `task_favorite_feature`: Tính năng bạn đánh giá cao nhất trong Soul Studio.
- `task_favorite_profile`: Profile giọng nói bạn cảm thấy ưng ý nhất.
- `task_ease_of_use_rating`: Điểm đánh giá độ dễ dùng từ 1 đến 5 (số nguyên).
