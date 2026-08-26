# Chatbot Task: Trợ lý Tâm sự & Đồng hành Biểu đạt Vita Soul (Soul Expressions & Companionship)

Task này kết nối các hồ sơ người dùng ảo (Persona) của MatrAIx trực tiếp tới khả năng biểu đạt cảm xúc qua giọng nói (Vita Soul) và trò chuyện đồng hành giải tỏa căng thẳng cho tài xế của **Trợ lý xe thông minh Vita** (`POST /api/chat` với `intent: casual_chat`, `drivingContext: alone` hoặc `traffic_jam`).

## Cấu hình kết nối (`input/chatbot.yaml`)

```yaml
transport: external_http
connection:
  baseUrlEnv: VITA_ASSISTANT_API_URL
  baseUrl: http://127.0.0.1:3001
  healthPath: /health
protocol:
  sendMessage:
    method: POST
    path: /api/chat
    staticBody:
      drivingContext: alone
      intent: casual_chat
```

## Khả năng kiểm thử chính

- Thử nghiệm 6 phong cách biểu đạt Vita Soul (`Normal`, `Sweet`, `Cheeky`, `Tươi sáng`, `Mộc mạc`, `Điềm tĩnh`).
- Thấu cảm cảm xúc và tâm trạng người lái: Nhận biết khi tài xế căng thẳng vì tắc đường, mệt mỏi sau ngày dài làm việc hoặc hào hứng trước chuyến đi.
- Giao tiếp đồng hành tự nhiên (Natural Companionship): Kể chuyện cười ngắn, đố vui nhẹ nhàng hoặc trò chuyện đồng hành mà không làm xao nhãng tay lái.
- Duy trì ngữ cảnh và ghi nhớ thói quen (Context Memory): Nhớ các chi tiết persona đã chia sẻ trong các lượt hội thoại trước.
