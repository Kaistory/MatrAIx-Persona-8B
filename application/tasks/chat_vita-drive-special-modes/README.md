# Chatbot Task: Trợ lý Chế độ Đặc biệt Xe Vita (Special Vehicle Modes)

Task này kết nối các hồ sơ người dùng ảo (Persona) của MatrAIx trực tiếp tới các chế độ vận hành chuyên dụng của **Trợ lý xe thông minh Vita** trên xe VinFast VF9 (`POST /api/chat` với `intent: vehicle_control`, `drivingContext: parked` hoặc `driving`).

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
      drivingContext: parked
      intent: vehicle_control
```

## Khả năng kiểm thử chính

- **Chế độ Rửa xe (Car Wash Mode)**: Tự động đóng kín toàn bộ cửa sổ & cửa sổ trời, khóa nắp cổng sạc, gập gương chiếu hậu ngoài, tắt gạt mưa tự động và cảm biến đỗ xe.
- **Chế độ Cắm trại (Camp Mode)**: Giữ điều hòa nhiệt độ thoải mái (22-24°C), duy trì nguồn điện khoang cabin, tắt đèn pha ngoại thất và màn hình giải trí ngoài để nghỉ ngơi qua đêm.
- **Chế độ Thú cưng (Pet Mode)**: Giữ nhiệt độ cabin mát mẻ an toàn khi người lái rời xe tạm thời, hiển thị thông báo an tâm cho người đi đường trên màn hình trung tâm.
- **Chế độ Trông xe / Giao xe (Valet Mode / Sentry Mode)**: Giới hạn tốc độ xe, khóa truy cập thông tin danh bạ/lịch sử hành trình và kích hoạt hệ thống camera giám sát an ninh xung quanh xe.
