# Chatbot Task: Trợ lý Giải trí & Âm nhạc Xe Vita (Infotainment & Media)

Task này kết nối các hồ sơ người dùng ảo (Persona) của MatrAIx trực tiếp tới năng lực giải trí và phát nhạc của **Trợ lý xe thông minh Vita** (`POST /api/chat` với `intent: music`, `drivingContext: passenger_present`).

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
    staticBody:
      drivingContext: passenger_present
      intent: music
```

## Khả năng kiểm thử chính

- Tìm kiếm và giải quyết bài hát qua Spotify & YouTube (`/api/media/resolve`).
- Phát âm và xác nhận tên bài hát/ca sĩ tự nhiên.
- Thích ứng trải nghiệm nghe nhạc theo ngữ cảnh có hành khách.
