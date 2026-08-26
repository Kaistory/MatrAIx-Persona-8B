# Vita Drive Assistant Chat Task

Task này kết nối các hồ sơ người dùng ảo (Persona) của MatrAIx trực tiếp tới hệ thống **Trợ lý xe thông minh Vita** (`vita-drive-assistant-lab`) đang chạy tại cổng `http://127.0.0.1:3001`.

## Cấu hình kết nối (`input/chatbot.yaml`)

```yaml
transport: external_http
connection:
  baseUrlEnv: VITA_ASSISTANT_API_URL
  baseUrl: http://127.0.0.1:3001
  healthPath: /health
protocol:
  sendMessage:
    method: POST
    path: /api/chat
    sessionIdField: sessionId
    messageField: message
    staticBody:
      drivingContext: driving
      intent: vehicle_control
  response:
    sessionIdField: sessionId
    replyField: assistantText
```

## Cách chạy

1. Đảm bảo server `vita-drive-assistant-lab` đang chạy (mặc định tại `http://127.0.0.1:3001`).
2. Mở Web Playground tại **http://localhost:3000** -> Chọn **Chat** -> **`chat_vita-drive-assistant`** -> **Run eval**.
