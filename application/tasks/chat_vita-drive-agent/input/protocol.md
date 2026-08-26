# Giao thức API Vita Agent Chat

- **Base URL**: `http://127.0.0.1:3001` (Tùy biến qua biến môi trường `VITA_ASSISTANT_API_URL`)
- **Health Check**: `GET /health`
- **Gửi tin nhắn Agent**: `POST /api/agent/chat`
  - Request: `{"message": "<lệnh người dùng>", "drivingContext": "driving", "intent": "vehicle_control", "history": [...]}`
  - Response: `{"assistantText": "<phản hồi của agent>", "metadata": {...}, "vehicle": {"results": [...], "state": {...}}}`
