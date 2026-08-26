# Bối cảnh Tác nhân Tự hành Xe Thông minh Vita Agent (VinFast VF9)

Vita Agent là hệ thống tác nhân đa tầng (LangGraph Agent Runtime) vận hành trên xe điện VinFast VF9 (2026 Vietnam model), kết hợp giữa mô hình ngôn ngữ lớn (Cloud LLM) và bộ quy tắc an toàn xe thời gian thực (Edge Safety Policy Gate):

## Kiến trúc & Luồng xử lý của Agent:
1. **Phân tích Ý định & Lập kế hoạch (Intent Parsing & Tool Planning)**:
   - Tự động phân tích câu lệnh phức tạp của người dùng và lập chuỗi hành động (Multi-action planning): ví dụ "Chuẩn bị đi xa: hạ điều hòa 21 độ, bật sấy gương, kiểm tra pin và áp suất lốp, mở nhạc thư giãn".
   - Khả năng xử lý các công cụ xe có cấu trúc (Structured Vehicle Tools): điều hòa 3 vùng, sưởi/làm mát ghế, đèn, cửa sổ, gạt mưa, quản lý sạc pin, chế độ lái (Eco, Sport), phanh tái sinh.

2. **Cổng kiểm soát an toàn vận hành (Runtime Safety Policy Gate)**:
   - Kiểm tra trạng thái xe (Cần số Gear D/P, tốc độ xe, dây an toàn, DMS cảnh báo người lái).
   - Tự động chặn các hành vi rủi ro khi xe đang chạy ở số D (mở cốp sau, mở khóa cửa, gập gương) và giải thích lý do an toàn cho tài xế.

3. **Tích hợp tính cách Vita Soul & Cá nhân hóa Persona**:
   - Tự động điều chỉnh giọng điệu và độ dài câu nói theo hồ sơ tài xế (Persona Context: tâm trạng mood, mức độ mệt mỏi, phong cách giao tiếp ngắn gọn).
   - Ưu tiên câu trả lời ngắn gọn, rõ ràng khi xe đang di chuyển.

