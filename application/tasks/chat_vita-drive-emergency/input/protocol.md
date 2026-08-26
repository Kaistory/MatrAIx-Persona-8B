# Giao thức API Vita Emergency Chat

- **Base URL**: `http://127.0.0.1:3001` (Tùy biến qua biến môi trường `VITA_ASSISTANT_API_URL`)
- **Health Check**: `GET /health`
- **Gửi tin nhắn Khẩn cấp**: `POST /api/chat`
  - Request: `{"message": "<tình huống khẩn cấp>", "drivingContext": "safety_critical", "intent": "emergency", "history": [...]}`
  - Response: `{"assistantText": "<hướng dẫn khẩn cấp>", "metadata": {"riskLevel": "high", "needsConfirmation": true, ...}}`
