# Khảo sát Trải nghiệm Trợ lý Xe Thông minh Vita

## Task instruction

# Khảo sát Trải nghiệm & Thái độ đối với Trợ lý Xe Thông minh Vita (Vita Drive Assistant Survey)

Bạn là người lái xe (hoặc người quan tâm đến ô tô thông minh) đang tham gia cuộc khảo sát ý kiến người dùng về hệ thống Trợ lý Giọng nói & Tác nhân Xe Thông minh (Vita Drive Assistant).

Hãy trả lời tất cả các câu hỏi một cách trung thực, phản ánh đúng đặc điểm nhân khẩu học, thói quen lái xe, thái độ đối với công nghệ AI và sự sẵn sàng chi trả của hồ sơ tính cách (Persona) của bạn.

## Context

# Bối cảnh Khảo sát Trợ lý Lái xe Thông minh Vita (Vita In-Cabin AI Survey)

Vita Drive Assistant là hệ thống trợ lý ảo và tác nhân thông minh tích hợp trên khoang lái ô tô điện thế hệ mới (Smart EV), hỗ trợ:
- Điều khiển phương tiện bằng giọng nói (điều hòa, cửa kính, ghế sưởi, đèn xe, chế độ lái).
- Dẫn đường thông minh, gợi ý trạm sạc xe điện tối ưu dọc lộ trình và tra cứu điểm quan tâm (POI).
- Giải trí thông minh (tìm kiếm bài hát trên Spotify/YouTube, đề xuất danh sách phát theo tâm trạng).
- Kiểm soát an toàn và hạn chế xao nhãng khi lái xe.

## Questionnaire

# Khảo sát Trải nghiệm Trợ lý Xe Thông minh Vita

Use exact `questionId` and valid choice ids.

## q0

Prompt: Bạn có thường xuyên sử dụng trợ lý giọng nói (Siri, Google Assistant, trợ lý tích hợp trên xe) khi đang lái xe không?

- Construct: `in_car_voice_assistant_frequency`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `daily` | Hàng ngày mỗi khi lái xe |
| `weekly` | Vài lần một tuần |
| `rarely` | Hiếm khi, chỉ khi thực sự cần thiết |
| `never` | Chưa bao giờ sử dụng |

## q1

Prompt: Khi đang lái xe trên đường, bạn ưu tiên phương thức điều khiển nào nhất để thao tác điều hòa, bản đồ hoặc bài hát?

- Construct: `primary_driving_interaction_mode`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `voice` | Giọng nói (Hands-free Voice Commands) |
| `physical_buttons` | Phím bấm vật lý trên vô lăng / táp-lô |
| `touchscreen` | Màn hình cảm ứng trung tâm |
| `passenger` | Nhờ người ngồi bên cạnh thao tác hộ |

## q2

Prompt: Mức độ an tâm của bạn khi ra lệnh giọng nói để điều khiển các chức năng vật lý của xe (điều hòa, cửa sổ, gạt mưa, đèn xe):

- Construct: `voice_vehicle_control_comfort`
- Type: `likert`
- Required: `true`
- Scale: `1`-`5`

Rate with an integer between **1** and **5**.


## q3

Prompt: Mức độ tin cậy của bạn vào tính năng AI tự động tính toán dung lượng pin và đề xuất trạm sạc xe điện tối ưu dọc lộ trình:

- Construct: `ev_routing_and_range_trust`
- Type: `likert`
- Required: `true`
- Scale: `1`-`5`

Rate with an integer between **1** and **5**.


## q4

Prompt: Tính năng tìm kiếm và phát nhạc theo tên bài hát / ca sĩ tiếng Việt qua giọng nói trên xe quan trọng với bạn như thế nào?

- Construct: `in_car_media_voice_importance`
- Type: `likert`
- Required: `true`
- Scale: `1`-`5`

Rate with an integer between **1** and **5**.


## q5

Prompt: Bạn mong muốn phong cách phản hồi giọng nói của trợ lý xe Vita như thế nào khi xe đang chạy?

- Construct: `preferred_voice_tone`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `concise` | Cực kỳ ngắn gọn, dứt khoát để không gây phân tâm lái xe |
| `friendly` | Tự nhiên, thân thiện và ấm áp |
| `professional` | Trang trọng, chuẩn mực và thông thái |
| `silent_action` | Chỉ thực thi trong im lặng, không cần phát âm xác nhận |

## q6

Prompt: Khi bạn yêu cầu thao tác có rủi ro (ví dụ: gọi điện khẩn cấp, mở cửa xe khi đang di chuyển), bạn đánh giá câu hỏi xác nhận an toàn của trợ lý ra sao?

- Construct: `safety_confirmation_attitude`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `essential` | Rất cần thiết, bắt buộc phải hỏi lại để đảm bảo an toàn tuyệt đối |
| `sensitive_only` | Chỉ cần thiết cho các thao tác cực kỳ nguy hiểm |
| `annoying` | Không cần thiết, gây mất thời gian — nên thực thi ngay |

## q7

Prompt: Mối bận tâm hoặc rủi ro lớn nhất của bạn đối với trợ lý AI trong khoang lái là gì? (Chọn tối đa 2)

- Construct: `in_cabin_ai_top_concerns`
- Type: `multi_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `distraction` | Gây xao nhãng hoặc mất tập trung khi lái xe |
| `misexecution` | Nhận diện sai giọng nói dẫn đến thực thi sai tính năng xe |
| `privacy` | Thu âm và thu thập dữ liệu riêng tư trong khoang lái |
| `latency` | Độ trễ phản hồi lâu khi cần thao tác khẩn cấp |
| `offline_failure` | Không hoạt động được khi xe đi vào vùng mất sóng/hầm |

## q8

Prompt: Nếu hệ thống Vita Drive Assistant cung cấp gói tính năng nâng cao (Tác nhân tự hành thông minh, dẫn đường thời gian thực không quảng cáo, gợi ý âm nhạc cá nhân hóa), bạn sẵn sàng chi trả ở mức nào?

- Construct: `ai_assistant_willingness_to_pay`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `free_only` | Chỉ dùng bản miễn phí cơ bản, không sẵn sàng trả thêm phí thuê bao |
| `basic_sub` | Khoảng 50.000 - 100.000 VNĐ / tháng ($2 - $4/tháng) |
| `premium_sub` | Khoảng 150.000 - 250.000 VNĐ / tháng ($6 - $10/tháng) |
| `one_time_bundle` | Sẵn sàng trả trọn gói 1 lần khi mua xe (5 - 10 triệu VNĐ) để dùng vĩnh viễn |

## q9

Prompt: Tầm quan trọng của tính năng xử lý cục bộ trên xe (Offline Edge AI - hoạt động không cần Internet):

- Construct: `offline_edge_ai_importance`
- Type: `likert`
- Required: `true`
- Scale: `1`-`5`

Rate with an integer between **1** and **5**.


## q10

Prompt: Trên thang điểm từ 0 đến 10, khả năng bạn sẽ giới thiệu một chiếc xe ô tô có trang bị Trợ lý Vita cho đồng nghiệp hoặc người thân là bao nhiêu?

- Construct: `nps_likelihood_recommend_vita`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `0` | 0 - Hoàn toàn không bao giờ |
| `1` | 1 |
| `2` | 2 |
| `3` | 3 |
| `4` | 4 |
| `5` | 5 - Bình thường |
| `6` | 6 |
| `7` | 7 |
| `8` | 8 |
| `9` | 9 |
| `10` | 10 - Chắc chắn sẽ giới thiệu |

## q11

Prompt: Loại phương tiện bạn đang sở hữu hoặc thường xuyên điều khiển nhất hiện nay:

- Construct: `vehicle_ownership_type`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `pure_ev` | Xe ô tô thuần điện (BEV) |
| `hybrid` | Xe ô tô Hybrid / Plug-in Hybrid |
| `ice` | Xe ô tô động cơ đốt trong (Xăng / Dầu) |
| `motorbike` | Xe máy |
| `none` | Chưa sở hữu phương tiện cá nhân |

## q12

Prompt: Thời gian lái xe trung bình mỗi ngày của bạn là bao lâu?

- Construct: `daily_driving_time`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `under_30m` | Dưới 30 phút / ngày |
| `30_to_60m` | Từ 30 đến 60 phút / ngày |
| `1_to_2h` | Từ 1 đến 2 tiếng / ngày |
| `over_2h` | Trên 2 tiếng / ngày (lái xe đường dài, dịch vụ) |

## Answer envelope

Platform-derived answer envelope (from `questionnaire.yaml`).

```json
{
  "instrument": {"id": "vita_drive_experience_v1", "title": "Khảo sát Trải nghiệm Trợ lý Xe Thông minh Vita"},
  "answers": [
    {
      "questionId": "q0",
      "value": "<answer value>"
    }
  ]
}
```

Use exact `questionId` values from the questionnaire.
For choice questions, `value` must be the exact choice id (or list of ids for multi-select).
Default surveys emit `questionId` + `value` only (choice / likert / bool).