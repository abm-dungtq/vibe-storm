<div align="center">

# ⚡ VIBE STORM SUITE

### Bộ 5 Kỹ Năng AI Agent Chuẩn Mực Cho Ý Tưởng Kinh Doanh, Marketing & Tăng Trưởng
*(Kiến trúc 5 giai đoạn độc lập: Brainstorm ➔ Research ➔ Scout ➔ Plan ➔ Cook)*

[![License: MIT](https://img.shields.io/badge/Gi%E1%BA%A5y%20ph%C3%A9p-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-5%20Skills%20Installed-blue)](https://code.claude.com)
[![Cursor](https://img.shields.io/badge/Cursor-5%20Rules%20Ready-purple)](https://cursor.com)
[![AgentSkills](https://img.shields.io/badge/Chu%E1%BA%A9n-AgentSkills.io-orange)](https://agentskills.io)
[![Pipeline](https://img.shields.io/badge/Pipeline-Brainstorm%E2%86%92Research%E2%86%92Scout%E2%86%92Plan%E2%86%92Cook-emerald)](https://github.com/abm-dungtq/vibe-storm)

*Đóng gói trọn vẹn 5 sub-skills độc lập vận hành xuyên suốt chuỗi cung ứng giá trị thương mại 5 bước: Đóng khung ý tưởng $\to$ Nghiên cứu đối thủ $\to$ Thám thính phễu $\to$ Lập kế hoạch phân kỳ $\to$ Thực thi chốt đơn.*

---

[Bộ 5 Kỹ Năng Độc Lập](#bo-5-ky-nang) • [Bản Hợp Đồng Bounded](#hop-dong-bounded) • [Chẩn Đoán Sự Cố Doanh Thu](#chan-doan-su-co) • [Cài Đặt & Sử Dụng](#cai-dat) • [Ví Dụ Thực Tế](#vi-du)

---

</div>

<a id="bo-5-ky-nang"></a>
## 🏛️ 1. Bộ 5 Kỹ Năng Độc Lập Cho Doanh Nhân & Solopreneur

Hệ thống cung cấp 5 công cụ độc lập, tương thích tuyệt đối với Claude Code, Cursor, Antigravity và Terminal CLI:

$$\mathbf{[vibe\text{-}storm]} \longrightarrow \mathbf{[vibe\text{-}research]} \longrightarrow \mathbf{[vibe\text{-}scout]} \longrightarrow \mathbf{[vibe\text{-}plan]} \longrightarrow \mathbf{[vibe\text{-}cook]}$$

| Bước | Lệnh Trực Tiếp | Bản Chất Nghiệp Vụ Trong Kinh Doanh |
| :---: | :--- | :--- |
| **1** | **`/vibe-storm`** | **Đóng Khung Hợp Đồng Thương Mại (Bounded Contract):** Khóa chặt 4 trường *Outcome, Constraints, Non-goals, Acceptance Criteria*; So sánh 3 phương án kinh doanh theo kịch bản xấu nhất; Chẩn đoán sự cố doanh thu (*Bug routing*). |
| **2** | **`/vibe-research`** | **Nghiên Cứu Thị Trường 4 Pha:** Khảo sát đối thủ cạnh tranh (tối đa 5 truy vấn sâu), bóc tách cấu trúc giá, phân tích khoảng trống giá trị (*Value Gap*), tìm kiếm rào cản mua hàng; xuất báo cáo `reports/research-*.md`. |
| **3** | **`/vibe-scout`** | **Thám Thính Hiện Trạng & Phễu:** Kiểm kê tài sản số sẵn có (email list, case studies), đo lường tỷ lệ rơi rụng khách hàng qua từng tầng phễu (*Funnel drop-off audit*); xuất báo cáo `reports/scout-*.md`. |
| **4** | **`/vibe-plan`** | **Lập Kế Hoạch Phân Kỳ (Files-First):** Khởi tạo cấu trúc `plans/<slug>/plan.md` cùng 4 phase (`phase-01-offer.md` đến `phase-04-launch.md`), ma trận nghiệm thu thương mại & bảng rủi ro. |
| **5** | **`/vibe-cook`** | **Thực Thi Sản Xuất & Chốt Đơn:** Chế tác từng phase theo kế hoạch: Viết sales copy, dựng landing page, cấu hình cổng thanh toán (Stripe/VietQR/SePay), tự động hóa gửi email và đo lường đơn hàng. |

---

<a id="hop-dong-bounded"></a>
## 📋 2. Bản Hợp Đồng Kinh Doanh Đóng Khung (Bounded Contract)

Khi bắt đầu bất kỳ một ý tưởng kinh doanh hay chiến dịch nào với `/vibe-storm`, hệ thống bắt buộc phải thiết lập bản hợp đồng 4 trường để chống bẫy phình to quy mô (scope creep):

- **🎯 Outcome:** Trạng thái đích thương mại đo lường được (Ví dụ: "10 khách hàng trả phí \$1,500/tháng, MRR \$15k sau 60 ngày").
- **🔒 Constraints:** Ràng buộc thực tế (Ngân sách \$0 tiền ads, hoàn thành trong 7 ngày, biên lợi nhuận ròng $\ge 80\%$).
- **🚫 Non-goals:** Phạm vi từ chối — Những việc **TUYỆT ĐỐI KHÔNG LÀM** (Không tuyển thêm nhân sự, không phát triển tính năng phụ rườm rà).
- **✅ Acceptance Criteria:** Bằng chứng nghiệm thu thực tế (Có 5 hợp đồng đặt cọc trước, trang đích đạt chuyển đổi $\ge 3\%$).

---

<a id="chan-doan-su-co"></a>
## 🔍 3. Chẩn Đoán Sự Cố Doanh Thu (Bug Routing)

Khi một chiến dịch kinh doanh bị tắc nghẽn (ads cắn tiền không ra đơn, landing page nhiều view nhưng không ai mua), `vibe-storm` áp dụng quy trình **Bug Routing** nghiêm ngặt — **chẩn đoán nguyên nhân gốc rễ trước khi sửa chữa**:

```mermaid
flowchart TD
    Issue[Sự cố: Doanh số tụt / Ads lỗ / Tắc phễu] --> Audit[vibe-scout: Thám thính toàn bộ hành trình khách hàng]
    Audit --> Q1{Tỷ lệ click CTR < 1.5%?}
    Q1 -->|Đúng| F1[Nguyên nhân: Hook yếu / Thông điệp lệch tệp -> Đổi góc đánh sáng tạo]
    Q1 -->|Sai| Q2{Tỷ lệ chuyển đổi trang < 2%?}
    Q2 -->|Đúng| F2[Nguyên nhân: Lời chào hàng Offer yếu / Thiếu bằng chứng tin cậy]
    Q2 -->|Sai| Q3{Tỷ lệ bỏ giỏ hàng > 70%?}
    Q3 -->|Đúng| F3[Nguyên nhân: Bỡ ngỡ về giá / Phí ẩn / Cổng thanh toán khó dùng]
    Q3 -->|Sai| F4[Nguyên nhân: Trải nghiệm nhận hàng kém / Tỷ lệ churn cao]
```

---

<a id="cai-dat"></a>
## 🚀 4. Hướng Dẫn Cài Đặt 1 Chạm

### Cách 1: Cài đặt tự động qua lệnh curl (Khuyên dùng)
```bash
curl -fsSL https://raw.githubusercontent.com/abm-dungtq/vibe-storm/main/scripts/install.sh | bash
```

### Cách 2: Clone repository và cài đặt thủ công
```bash
git clone https://github.com/abm-dungtq/vibe-storm.git
cd vibe-storm
bash scripts/install.sh
```

Lệnh trên sẽ tự động:
- Cài đặt trọn bộ 5 skills vào **Claude Code** (`~/.claude/skills/`).
- Cài đặt trọn bộ 5 skills vào **Antigravity / Gemini CLI** (`~/.gemini/config/skills/`).
- Kích hoạt 5 rules tương ứng trong **Cursor IDE** (`.cursor/rules/`).

---

<a id="vi-du"></a>
## 💻 5. Ví Dụ Câu Lệnh Thực Chiến Cho Từng Bước

Bạn có thể chạy toàn bộ quy trình liên hoàn hoặc gọi riêng lẻ từng bước tùy theo tình huống:

### Bước 1: Khởi tạo ý tưởng & Đóng khung hợp đồng
```bash
/vibe-storm "Dịch vụ AI Ops tự động hóa chăm sóc khách hàng cho phòng khám nha khoa" --biz --html
```

### Bước 2: Nghiên cứu thị trường & Bóc tách đối thủ
```bash
/vibe-research "Thị trường phần mềm và dịch vụ đặt lịch hẹn tự động cho nha khoa tại Việt Nam"
```

### Bước 3: Thám thính phễu & Rà soát điểm nghẽn
```bash
/vibe-scout "Landing page đặt lịch hẹn nha khoa hiện tại đang có tỷ lệ thoát 85%"
```

### Bước 4: Lập kế hoạch hành động phân kỳ 4 Phase
```bash
/vibe-plan "Kế hoạch ra mắt dịch vụ đóng gói AI Ops trong 7 ngày" --html
```

### Bước 5: Thực thi sản xuất tài sản & Chốt đơn
```bash
/vibe-cook ./plans/260904-launch-ai-ops/plan.md --interactive
```

---

## 🗂️ 6. Cấu Trúc Repository Đầy Đủ

```text
vibe-storm/
├── .claude-plugin/           # Plugin catalog đăng ký trọn bộ 5 skills
├── .cursor/rules/            # 5 file rule mdc tương ứng cho Cursor IDE
├── skills/
│   ├── vibe-storm/           # [Bước 1] Brainstorm & Điều phối
│   ├── vibe-research/        # [Bước 2] Market & Competitor Research
│   ├── vibe-scout/           # [Bước 3] Funnel & Asset Scout
│   ├── vibe-plan/            # [Bước 4] Phased Business Planning
│   └── vibe-cook/            # [Bước 5] Commercial Execution & Production
├── templates/
│   └── vibe-board-template.html
├── scripts/
│   ├── install.sh            # Cài đặt trọn bộ 5 skills (hỗ trợ cả curl pipe)
│   ├── quick_validate.py     # Kiểm tra tính hợp lệ của cả 5 skills
│   └── generate_board.py     # CLI sinh file HTML an toàn không lo XSS
└── README.md
```

---

## 🤝 Giấy Phép

Phát hành dưới giấy phép mã nguồn mở **[MIT License](LICENSE)**.  
Được phát triển bởi **[abm-dungtq](https://github.com/abm-dungtq)**.
