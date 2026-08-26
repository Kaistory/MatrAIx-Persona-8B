# Giao thức API Vita Communication Chat

- **Base URL**: `http://127.0.0.1:3001` (Tùy biến qua biến môi trường `VITA_ASSISTANT_API_URL`)
- **Health Check**: `GET /health`
- **Gửi tin nhắn Liên lạc**: `POST /api/chat`
  - Request: `{"message": "<lệnh gọi điện/nhắn tin>", "drivingContext": "driving", "intent": "message", "history": [...]}`
  - Response: `{"assistantText": "<xác nhận của trợ lý>", "metadata": {"needsConfirmation": true, "needsPermission": true, ...}}`
