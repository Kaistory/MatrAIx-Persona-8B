# Trải nghiệm Dashboard Xe Thông Minh Vita Drive Assistant

Đọc bối cảnh trong `input/context.md`, truy cập http://172.17.0.1:5173/ (nếu có màn hình đăng nhập, nhập mật khẩu là "dev" rồi bấm nút "Đăng nhập" để vào) và tương tác với giao diện buồng lái xe thông minh.

Sau khi trải nghiệm các tính năng trên website, hãy lưu kết quả quyết định và đánh giá của bạn vào `/app/output/dashboard_experience.json`:

```json
{
  "decision_subject_id": "vita_car_dashboard",
  "decision_subject_label": "Vita Drive Assistant Dashboard",
  "decision_outcome": "selected",
  "basis_primary": "<convenience|features|quality|taste|trust|familiarity|novelty|fit|other>",
  "exploration_style": "<quick_pick|compared_multiple|deep_research|hesitant>",
  "reason": "<Cảm nhận chi tiết của bạn về giao diện, tính năng điều khiển và trợ lý xe>",
  "task_favorite_feature": "<tính năng bạn thích nhất, ví dụ: climate_control, navigation, music_player, vehicle_controls, voice_assistant>",
  "task_ease_of_use_rating": 5
}
```

Yêu cầu:
- `basis_primary`: Yếu tố chính ảnh hưởng đến đánh giá của bạn (ví dụ: `convenience`, `features`, `quality`, `fit`,...).
- `exploration_style`: Phong cách duyệt và khám phá dashboard của bạn (ví dụ: `compared_multiple`, `deep_research`, `quick_pick`).
- `reason`: Nêu rõ lý do dưới góc nhìn cá nhân (persona) của bạn.
- `task_favorite_feature`: Tính năng bạn đánh giá cao nhất trên giao diện.
- `task_ease_of_use_rating`: Điểm đánh giá độ dễ dùng từ 1 đến 5 (số nguyên).
