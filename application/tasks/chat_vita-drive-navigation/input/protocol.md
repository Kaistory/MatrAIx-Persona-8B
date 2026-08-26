# Giao thức API Vita Navigation Chat

- **Base URL**: `http://127.0.0.1:3001` (Tùy biến qua biến môi trường `VITA_ASSISTANT_API_URL`)
- **Health Check**: `GET /health`
- **Gửi tin nhắn Dẫn đường**: `POST /api/chat`
  - Request: `{"message": "<yêu cầu tìm đường/địa điểm>", "drivingContext": "driving", "intent": "navigation", "history": [...]}`
  - Response: `{"assistantText": "<chỉ dẫn của trợ lý>", "metadata": {...}, "vehicle": {...}}`
