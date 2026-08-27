# Trải nghiệm Scenario Playground & Evaluation Lab (VinFast VF9)

Truy cập địa chỉ `https://192.168.137.242:5173/` (nếu có màn hình đăng nhập, nhập mật khẩu là `dev` rồi bấm nút **"Đăng nhập"**), sau đó chọn tab **"Thử nghiệm" (Playground)** trên thanh menu chính để khám phá bảng thử nghiệm kịch bản lái xe và đánh giá tự động của trợ lý Vita.

### Nhiệm vụ của bạn:
1. **Khám phá Scenario Playground & Đánh giá**:
   - **Bộ chọn kịch bản lái xe (Scenario Selector)**: Lựa chọn các tình huống lái xe đa dạng (Ví dụ: *"Kẹt xe tan tầm - Cần thư giãn"*, *"Lái xe đường đèo ban đêm"*, *"Sạc pin EV trên cao tốc"*, *"Tình huống khẩn cấp - Cảnh báo lốp"*).
   - **Gửi lệnh & Quan sát phân luồng (Turn Execution & Routing)**: Nhập lệnh hoặc chọn câu mẫu, quan sát hệ thống tự động nhận diện ý định (Intent), phân loại ngữ cảnh lái xe và chọn nhánh xử lý (Edge Fast Path vs Cloud LLM Stream).
   - **Bảng kiểm tra quy tắc (Rule Checklist & Policy)**: Quan sát danh sách kiểm tra các quy tắc an toàn, mức độ tuân thủ chính sách xe (VF9 Safety Policy) và rào chắn cấp số Gear.
   - **Kết quả chấm điểm AI Judge (Evaluation Card)**: Xem điểm số đánh giá từ bộ chấm quy tắc (Deterministic Evaluator) và giám khảo AI (AI Judge) về độ chính xác, an toàn và giọng điệu.
   - **Công cụ xuất dữ liệu (Batch / QA Export)**: Khám phá các tùy chọn xuất lịch sử hội thoại kiểm thử để phục vụ phân tích dữ liệu.

2. **Lưu đánh giá**:
   Sau khi trải nghiệm các tính năng trong Scenario Playground, hãy đóng vai Persona của bạn để lưu kết quả đánh giá vào `/app/output/playground_experience.json`:

```json
{
  "decision_subject_id": "vita_scenario_playground",
  "decision_subject_label": "Vita Scenario Playground & Evaluation Lab",
  "decision_outcome": "selected",
  "basis_primary": "<convenience|features|quality|taste|trust|familiarity|novelty|fit|other>",
  "exploration_style": "<quick_pick|compared_multiple|deep_research|hesitant>",
  "reason": "<Cảm nhận chi tiết của bạn về tính thực tế của các kịch bản lái xe, độ hữu ích của Rule Checklist, sự minh bạch của AI Judge và trải nghiệm thử nghiệm tổng thể>",
  "task_favorite_feature": "<tính năng bạn thích nhất, ví dụ: scenario_selection, edge_cloud_routing_display, rule_checklist, ai_judge_evaluation, qa_batch_export>",
  "task_favorite_scenario": "<kịch bản bạn cảm thấy thú vị nhất>",
  "task_ease_of_use_rating": 5
}
```

Yêu cầu:
- `basis_primary`: Yếu tố chính ảnh hưởng đến đánh giá của bạn (ví dụ: `features`, `quality`, `trust`, `convenience`, `fit`,...).
- `exploration_style`: Phong cách khám phá của bạn (`quick_pick`, `compared_multiple`, `deep_research`, `hesitant`).
- `reason`: Nêu rõ lý do dưới góc nhìn cá nhân (persona) của bạn.
- `task_favorite_feature`: Tính năng bạn đánh giá cao nhất trong Scenario Playground.
- `task_favorite_scenario`: Tên kịch bản lái xe bạn ấn tượng nhất.
- `task_ease_of_use_rating`: Điểm đánh giá độ dễ dùng từ 1 đến 5 (số nguyên).
