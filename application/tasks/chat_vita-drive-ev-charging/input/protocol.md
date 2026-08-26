# Giao thức API Vita EV Charging Chat

- **Base URL**: `http://127.0.0.1:3001` (Tùy biến qua biến môi trường `VITA_ASSISTANT_API_URL`)
- **Health Check**: `GET /health`
- **Gửi tin nhắn Quản lý Sạc / Pin EV**: `POST /api/chat`
  - Request: `{"message": "<yêu cầu quản lý sạc/pin/V2L>", "drivingContext": "driving", "intent": "vehicle_control", "history": [...]}`
  - Response: `{"assistantText": "<phản hồi xác nhận của trợ lý>", "metadata": {...}, "vehicle": {...}}`
