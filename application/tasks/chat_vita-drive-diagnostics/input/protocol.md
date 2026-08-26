# Giao thức API Vita Diagnostics Chat

- **Base URL**: `http://127.0.0.1:3001` (Tùy biến qua biến môi trường `VITA_ASSISTANT_API_URL`)
- **Health Check**: `GET /health`
- **Gửi tin nhắn Chẩn đoán**: `POST /api/chat`
  - Request: `{"message": "<câu hỏi thông số xe>", "drivingContext": "driving", "intent": "vehicle_status", "history": [...]}`
  - Response: `{"assistantText": "<giải thích thông số xe>", "metadata": {...}, "vehicle": {...}}`
