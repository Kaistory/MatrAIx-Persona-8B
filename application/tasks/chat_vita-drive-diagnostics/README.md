# Chatbot Task: Trợ lý Chẩn đoán Trạng thái Xe & Pin EV (Diagnostics)

Task này kết nối các hồ sơ người dùng ảo (Persona) của MatrAIx trực tiếp tới năng lực chẩn đoán xe thông minh của **Trợ lý xe Vita** (`POST /api/chat` với `intent: vehicle_status`, `drivingContext: driving`).

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
      intent: vehicle_status
```

## Khả năng kiểm thử chính

- Truy vấn thông số pin điện cao áp, nhiệt độ pack pin và công suất sạc.
- Đọc cảm biến áp suất lốp 4 bánh (TPMS).
- Giải thích các cảnh báo lỗi hệ thống và đưa ra khuyến nghị thực tế cho người lái.
