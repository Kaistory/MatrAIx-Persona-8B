# Giao thức API Vita Climate & Comfort Chat

- **Base URL**: `http://127.0.0.1:3001` (Tùy biến qua biến môi trường `VITA_ASSISTANT_API_URL`)
- **Health Check**: `GET /health`
- **Gửi tin nhắn Điều hòa / Tiện nghi**: `POST /api/chat`
  - Request: `{"message": "<yêu cầu chỉnh điều hòa/ghế>", "drivingContext": "driving", "intent": "vehicle_control", "history": [...]}`
  - Response: `{"assistantText": "<phản hồi xác nhận của trợ lý>", "metadata": {...}, "vehicle": {...}}`
