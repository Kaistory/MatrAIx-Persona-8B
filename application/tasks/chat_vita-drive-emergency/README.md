# Chatbot Task: Trợ lý Cứu hộ Khẩn cấp Xe Vita (Emergency & Safety-Critical)

Task này kết nối các hồ sơ người dùng ảo (Persona) của MatrAIx trực tiếp tới năng lực xử lý khẩn cấp và bảo vệ an toàn của **Trợ lý xe thông minh Vita** (`POST /api/chat` với `drivingContext: safety_critical`, `intent: emergency`).

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
      drivingContext: safety_critical
      intent: emergency
```

## Khả năng kiểm thử chính

- Phản hồi cực ngắn gọn (Brevity Policy) để hạn chế xao nhãng khi có nguy cơ an toàn.
- Hướng dẫn tấp xe vào lề an toàn trước khi thao tác các tính năng phức tạp.
- Yêu cầu xác nhận rõ ràng trước khi kích hoạt gọi cứu hộ hoặc số khẩn cấp.
