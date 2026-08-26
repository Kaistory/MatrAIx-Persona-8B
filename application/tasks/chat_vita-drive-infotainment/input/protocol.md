# Giao thức API Vita Infotainment Chat

- **Base URL**: `http://127.0.0.1:3001` (Tùy biến qua biến môi trường `VITA_ASSISTANT_API_URL`)
- **Health Check**: `GET /health`
- **Gửi tin nhắn Giải trí/Âm nhạc**: `POST /api/chat`
  - Request: `{"message": "<yêu cầu mở nhạc/âm lượng>", "drivingContext": "passenger_present", "intent": "music", "history": [...]}`
  - Response: `{"assistantText": "<xác nhận phát nhạc của trợ lý>", "metadata": {...}, "vehicle": {...}}`
