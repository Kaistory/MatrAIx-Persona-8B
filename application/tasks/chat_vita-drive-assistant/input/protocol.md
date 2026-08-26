# Giao thức API Trợ lý Vita

- **Base URL**: `http://127.0.0.1:3001` (Tùy biến qua biến môi trường `VITA_ASSISTANT_API_URL`)
- **Health Check**: `GET /health`
- **Gửi tin nhắn**: `POST /api/chat`
  - Request: `{"message": "<câu lệnh của người dùng>", "drivingContext": "driving", "intent": "vehicle_control"}`
  - Response: `{"assistantText": "<câu trả lời của Vita>", "metadata": {...}, "vehicle": {...}}`
