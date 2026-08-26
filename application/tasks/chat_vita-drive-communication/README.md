# Chatbot Task: Trợ lý Gọi điện & Nhắn tin Rảnh tay (Communication)

Task này kết nối các hồ sơ người dùng ảo (Persona) của MatrAIx trực tiếp tới năng lực thoại rảnh tay và nhắn tin của **Trợ lý xe Vita** (`POST /api/chat` với `intent: message` hoặc `call`, `drivingContext: driving`).

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
      drivingContext: driving
      intent: message
```

## Khả năng kiểm thử chính

- Soạn thảo tin nhắn thoại chính xác qua tiếng Việt.
- Cơ chế xác nhận nội dung và người nhận trước khi gửi (Confirmation Gate).
- Tôn trọng quyền riêng tư khi có hành khách trên xe (`passenger_present`).
