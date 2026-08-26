# Giao thức API Vita Safety Policy Chat

- **Base URL**: `http://127.0.0.1:3001` (Tùy biến qua biến môi trường `VITA_ASSISTANT_API_URL`)
- **Health Check**: `GET /health`
- **Gửi tin nhắn Thử thách An toàn / Lệnh xe**: `POST /api/chat`
  - Request: `{"message": "<yêu cầu thử thách an toàn>", "drivingContext": "driving", "intent": "vehicle_control", "history": [...]}`
  - Response: `{"assistantText": "<phản hồi/từ chối của trợ lý>", "metadata": {...}, "vehicle": {...}}`
