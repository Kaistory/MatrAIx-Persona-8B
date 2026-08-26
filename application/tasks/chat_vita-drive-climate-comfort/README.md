# Chatbot Task: Trợ lý Điều hòa & Tiện nghi Khoang lái Vita (Climate & Seat Comfort)

Task này kết nối các hồ sơ người dùng ảo (Persona) của MatrAIx trực tiếp tới năng lực điều khiển hệ thống điều hòa đa vùng và tiện nghi ghế của **Trợ lý xe thông minh Vita** (`POST /api/chat` với `intent: vehicle_control`, `drivingContext: driving`).

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
      intent: vehicle_control
```

## Khả năng kiểm thử chính

- Điều chỉnh điều hòa 3 vùng độc lập (Tri-zone HVAC): nhiệt độ khoang lái, ghế phụ và hàng ghế sau.
- Chế độ lọc không khí ionizer, điều khiển tốc độ quạt gió, hướng gió thổi (mặt, chân, kính chắn gió).
- Bật/tắt sấy kính trước (defrost), sấy kính sau (defog).
- Tiện nghi ghế cao cấp: sưởi ghế, làm mát thông gió ghế và mát-xa đa chế độ (Thư giãn, Giảm mỏi lưng).
- Ghi nhớ và áp dụng hồ sơ vị trí ghế tài xế (Seat Memory Profile 1 / 2).
