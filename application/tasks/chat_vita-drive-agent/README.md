# Chatbot Task: Trợ lý Tác nhân Tự hành Vita (In-Cabin Autonomous Agent)

Task này kết nối các hồ sơ người dùng ảo (Persona) của MatrAIx trực tiếp tới endpoint tác nhân tự hành **Vita Agent** (`POST /api/agent/chat`) thuộc hệ thống `vita-drive-assistant-lab` (mặc định tại `http://127.0.0.1:3001`).

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
    path: /api/agent/chat
```

## Khả năng kiểm thử chính

- Lập kế hoạch thực thi công cụ xe thông minh (Vehicle Tool Execution).
- Cơ chế kiểm soát an toàn và rủi ro (Policy Gate & Confirmation).
- Khả năng duy trì ngữ cảnh trạng thái xe đa lượt hội thoại.
