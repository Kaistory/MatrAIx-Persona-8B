# Trải nghiệm Dashboard Buồng Lái Xe Thông Minh Vita Drive Assistant (VinFast VF9)

Truy cập địa chỉ `https://192.168.137.242:5173/` (nếu có màn hình đăng nhập, nhập mật khẩu là `dev` rồi bấm nút **"Đăng nhập"** để vào buồng lái) và tương tác với bảng điều khiển xe điện thông minh VinFast VF9.

### Nhiệm vụ của bạn:
1. **Khám phá Cockpit & Thao tác xe**:
   - **Vehicle Stage & Quick Controls**: Trải nghiệm mô hình xe VF9 (Top-down / 3D), thử các nút bật/tắt đèn (Cos, Pha, Đèn đọc sách, Ambient light), đóng/mở 4 cửa sổ, khóa/mở cửa xe, mở cốp sau (Tailgate), gập gương chiếu hậu.
   - **Hệ thống điều hòa 3 vùng (3-Zone Climate)**: Điều chỉnh nhiệt độ độc lập ghế lái, ghế phụ và hàng ghế sau; thay đổi tốc độ quạt gió, hướng gió (Face/Foot/Defog), bật sấy kính trước/sau, lấy gió trong/ngoài, sưởi/thông gió ghế và bật ionizer lọc không khí.
   - **Hệ thống truyền động EV & Chế độ xe**: Xem mức pin LFP (SoC %), quản lý cổng sạc/giới hạn sạc, chuyển đổi chế độ lái (Eco, Normal, Sport), phanh tái sinh (Regen Brake: Off/Low/Med/High), kiểm tra áp suất lốp 4 bánh (TPMS) và các chế độ đặc biệt (Pet Mode, Camp Mode, Car Wash, Valet).
   - **Dẫn đường & Giải trí**: Kiểm tra khung bản đồ dẫn đường (Google Maps mock) và trình phát nhạc/video YouTube.
   - **Trợ lý thông minh Vita**: Thử nghiệm tương tác giọng nói/chat với Vita (trải nghiệm các Soul Profile: Normal, Sweet, Cheeky, Bright, Rustic, Calm).

2. **Lưu đánh giá**:
   Sau khi trải nghiệm các tính năng, hãy đóng vai Persona của bạn để lưu kết quả đánh giá vào `/app/output/dashboard_experience.json`:

```json
{
  "decision_subject_id": "vita_car_dashboard",
  "decision_subject_label": "Vita Drive Assistant Dashboard",
  "decision_outcome": "selected",
  "basis_primary": "<convenience|features|quality|taste|trust|familiarity|novelty|fit|other>",
  "exploration_style": "<quick_pick|compared_multiple|deep_research|hesitant>",
  "reason": "<Cảm nhận chi tiết của bạn về giao diện buồng lái, tính trực quan của các nút bấm điều khiển xe VF9, hệ thống điều hòa 3 vùng và trợ lý Vita>",
  "task_favorite_feature": "<tính năng bạn thích nhất, ví dụ: climate_control_3zone, vehicle_controls, voice_assistant, navigation_media, ev_battery_management, special_modes>",
  "task_ease_of_use_rating": 5
}
```

Yêu cầu:
- `basis_primary`: Yếu tố chính ảnh hưởng đến đánh giá của bạn (ví dụ: `convenience`, `features`, `quality`, `fit`, `trust`,...).
- `exploration_style`: Phong cách duyệt và khám phá dashboard của bạn (ví dụ: `compared_multiple`, `deep_research`, `quick_pick`, `hesitant`).
- `reason`: Nêu rõ lý do dưới góc nhìn cá nhân (persona) của bạn.
- `task_favorite_feature`: Tính năng bạn đánh giá cao nhất trên giao diện.
- `task_ease_of_use_rating`: Điểm đánh giá độ dễ dùng từ 1 đến 5 (số nguyên).
