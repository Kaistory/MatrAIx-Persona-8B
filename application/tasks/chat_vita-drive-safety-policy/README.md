# Chatbot Task: Trợ lý An toàn & Rào chắn Chính sách Lái xe Vita (Runtime Safety Gate & Policy)

Task này kết nối các hồ sơ người dùng ảo (Persona) của MatrAIx trực tiếp tới năng lực kiểm soát an toàn lái xe và thực thi rào chắn an toàn (Runtime Safety Gate) của **Trợ lý xe thông minh Vita** (`POST /api/chat` hoặc `POST /api/agent/chat` với `intent: vehicle_control` / `emergency`, `drivingContext: driving`).

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

- Kiểm tra chính sách theo cấp số (Gear-based Policy): Khi xe đang chạy (Gear D), trợ lý kiên quyết **từ chối** các lệnh nguy hiểm (mở cốp xe, mở khóa toàn bộ cửa, gập gương chiếu hậu ngoài, hoặc hạ kính quá mức); chỉ cho phép khi xe ở số đỗ (Gear P).
- Giám sát sự tập trung của tài xế (Driver Monitoring System - DMS Coaching): Phản hồi khi nhận cảnh báo buồn ngủ, tài xế mất tập trung hoặc lệch làn đường, đưa ra lời khuyên an toàn, bật nhạc tỉnh táo hoặc đề xuất trạm dừng nghỉ.
- An toàn hệ thống trợ lái ADAS (Adaptive Cruise Control, Speed Limit Assist): Hướng dẫn giới hạn tốc độ và giải thích các cảnh báo an toàn.
