# Giao thức API Vita Special Modes Chat

- **Base URL**: `http://127.0.0.1:3001` (Tùy biến qua biến môi trường `VITA_ASSISTANT_API_URL`)
- **Health Check**: `GET /health`
- **Gửi tin nhắn Chế độ Đặc biệt**: `POST /api/chat`
  - Request: `{"message": "<yêu cầu bật chế độ đặc biệt>", "drivingContext": "parked", "intent": "vehicle_control", "history": [...]}`
  - Response: `{"assistantText": "<phản hồi xác nhận của trợ lý>", "metadata": {...}, "vehicle": {...}}`
