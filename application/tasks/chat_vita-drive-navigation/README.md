# Chatbot Task: Trợ lý Dẫn đường & Lộ trình Xe Vita (Navigation & EV Routing)

Task này kết nối các hồ sơ người dùng ảo (Persona) của MatrAIx trực tiếp tới năng lực dẫn đường và tìm trạm sạc của **Trợ lý xe thông minh Vita** (`POST /api/chat` với `intent: navigation`, `drivingContext: driving`).

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
      intent: navigation
```

## Khả năng kiểm thử chính

- Tính toán lộ trình VietMap / OSRM và phản hồi hướng đi rẽ rõ ràng.
- Tra cứu địa danh, POI và trạm sạc điện dọc tuyến.
- Phản hồi an toàn, ngắn gọn theo tiêu chuẩn trợ lý lái xe.
