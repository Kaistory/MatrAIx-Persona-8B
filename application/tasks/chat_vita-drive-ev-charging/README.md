# Chatbot Task: Trợ lý Sạc Pin EV & Năng lượng Vita (EV Charging & Energy Management)

Task này kết nối các hồ sơ người dùng ảo (Persona) của MatrAIx trực tiếp tới năng lực quản lý sạc pin, lập lịch sạc và tính năng năng lượng xe điện của **Trợ lý xe thông minh Vita** (`POST /api/chat` với `intent: vehicle_control` / `vehicle_status`, `drivingContext: driving` hoặc `charging`).

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

- Điều khiển mở/đóng nắp cổng sạc điện tử (Charge port door).
- Cài đặt giới hạn sạc mục tiêu (Target SoC limit: 80% để bảo vệ tuổi thọ pin LFP hoặc 100% cho chuyến đi xa).
- Thiết lập lịch sạc tự động giờ thấp điểm (Scheduled Charging).
- Quản lý tính năng cấp nguồn ngoại vi V2L (Vehicle-to-Load: cấp điện 220V cho thiết bị cắm trại / gia dụng).
- Kích hoạt chế độ chuẩn bị nhiệt độ pin (Battery Pre-conditioning) tối ưu tốc độ sạc trước khi đến trạm sạc siêu nhanh DC.
