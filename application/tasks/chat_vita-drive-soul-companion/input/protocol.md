# Giao thức API Vita Soul Companion Chat

- **Base URL**: `http://127.0.0.1:3001` (Tùy biến qua biến môi trường `VITA_ASSISTANT_API_URL`)
- **Health Check**: `GET /health`
- **Gửi tin nhắn Tâm sự / Đồng hành**: `POST /api/chat`
  - Request: `{"message": "<lời tâm sự/trò chuyện của persona>", "drivingContext": "alone", "intent": "casual_chat", "history": [...]}`
  - Response: `{"assistantText": "<phản hồi đồng cảm của trợ lý>", "metadata": {...}, "vehicle": {...}}`
