# Phân Tích Cụm Khách Hàng Từ Luật Kết Hợp (Association Rules)

## Tổng Quan Dự Án

Dự án này phân tích dữ liệu giao dịch bán lẻ từ một cửa hàng trực tuyến ở Vương Quốc Anh. Chúng tôi sử dụng kỹ thuật khai thác luật kết hợp (Apriori và FP-Growth) để tìm ra các mối quan hệ giữa các sản phẩm, sau đó sử dụng các luật này làm đặc trưng để phân cụm khách hàng bằng thuật toán K-Means.

## Phương Pháp

### 1. Chuẩn Bị Dữ Liệu
- Dữ liệu gốc: 541,909 giao dịch từ 4,372 khách hàng
- Làm sạch: Loại bỏ giao dịch không hợp lệ, tập trung vào khách hàng UK
- Tính RFM: Recency, Frequency, Monetary cho mỗi khách hàng

### 2. Khai Thác Luật Kết Hợp
- Sử dụng Apriori và FP-Growth để tìm luật kết hợp
- Top luật theo lift: Các sản phẩm thường được mua cùng nhau
- Ví dụ: HERB MARKER PARSLEY → HERB MARKER THYME (lift = 74.57)

### 3. Phân Cụm Từ Luật
- Chuyển đổi luật thành đặc trưng nhị phân cho mỗi khách hàng
- Kết hợp với RFM để tạo vector đặc trưng
- Áp dụng K-Means với k=2 clusters

## Kết Quả Phân Cụm

### Cluster 0: "Casual Shoppers" (Người Mua Lẻ)
- **Số lượng:** 3,797 khách hàng (97% tổng số)
- **RFM trung bình:**
  - Recency: 93.22 ngày
  - Frequency: 4.05 lần mua
  - Monetary: 1,809.82 GBP
- **RFM trung vị:**
  - Recency: 75 ngày
  - Frequency: 3 lần mua
  - Monetary: 1,200 GBP
- **Top Rules kích hoạt:** (dựa trên activation rate)
  1. WOODEN STAR CHRISTMAS SCANDINAVIAN -> WOODEN TREE CHRISTMAS SCANDINAVIAN (activation: 2.463)
  2. WOODEN HEART CHRISTMAS SCANDINAVIAN -> WOODEN STAR CHRISTMAS SCANDINAVIAN (activation: 2.163)
  3. WOODEN HEART CHRISTMAS SCANDINAVIAN -> WOODEN TREE CHRISTMAS SCANDINAVIAN (activation: 2.107)
  4. WOODEN STAR CHRISTMAS SCANDINAVIAN -> WOODEN HEART CHRISTMAS SCANDINAVIAN (activation: 2.099)
  5. WOODEN HEART CHRISTMAS SCANDINAVIAN, WOODEN STAR CHRISTMAS SCANDINAVIAN -> WOODEN TREE CHRISTMAS SCANDINAVIAN (activation: 2.004)
- **Persona:** Khách hàng mua sắm thông thường, ít tần suất, chi tiêu thấp, mua cách đây khá lâu.
- **Chiến lược marketing:**
  - Cross-sell: Đề xuất sản phẩm liên quan như Scandinavian Christmas decorations khi khách mua
  - Khuyến mãi: Giảm giá bundle để tăng tần suất mua
  - Kích hoạt ngủ đông: Email campaigns nhắc nhở mua lại sau thời gian dài

### Cluster 1: "VIP Customers" (Khách Hàng VIP)
- **Số lượng:** 124 khách hàng (3% tổng số)
- **RFM trung bình:**
  - Recency: 60.54 ngày
  - Frequency: 21.30 lần mua
  - Monetary: 17,365.53 GBP
- **RFM trung vị:**
  - Recency: 45 ngày
  - Frequency: 18 lần mua
  - Monetary: 15,000 GBP
- **Top Rules kích hoạt:** (dựa trên activation rate)
  1. HERB MARKER THYME -> HERB MARKER ROSEMARY (activation: 70.830)
  2. HERB MARKER ROSEMARY -> HERB MARKER THYME (activation: 70.244)
  3. HERB MARKER PARSLEY -> HERB MARKER CHIVES  (activation: 69.874)
  4. HERB MARKER PARSLEY, HERB MARKER THYME -> HERB MARKER ROSEMARY (activation: 69.454)
  5. HERB MARKER THYME -> HERB MARKER PARSLEY (activation: 69.415)
- **Persona:** Khách hàng thân thiết, mua nhiều, chi tiêu cao, tương tác gần đây.
- **Chiến lược marketing:**
  - VIP Program: Ưu đãi độc quyền, early access, personalized service
  - Bundle Deals: Gói sản phẩm tùy chỉnh với herb markers và sản phẩm liên quan
  - Cross-sell: Gợi ý sản phẩm dựa trên lịch sử mua
  - Loyalty Rewards: Tích điểm đổi quà, exclusive events

## Dashboard Streamlit

Chúng tôi đã xây dựng một dashboard tương tác sử dụng Streamlit với các tính năng:

- **Lọc theo cluster:** Chọn cụm 0 hoặc 1 để xem thông tin chi tiết
- **Thống kê RFM:** Hiển thị số lượng khách hàng và giá trị trung bình Recency, Frequency, Monetary
- **Phân bố RFM:** Biểu đồ histogram cho Recency
- **Top Rules per cluster:** Hiển thị 5 luật kết hợp hàng đầu được kích hoạt nhiều nhất trong cụm
- **Persona và chiến lược:** Mô tả đặc điểm khách hàng và chiến lược marketing phù hợp
- **Gợi ý Bundle/Cross-sell:** Đề xuất dựa trên luật kết hợp hàng đầu của cụm

Dashboard chạy tại: `streamlit run app.py`

## Kết Luận

Phân tích này cho thấy cách sử dụng luật kết hợp để tạo đặc trưng phong phú cho phân cụm khách hàng. Cluster VIP (Cluster 1) dù ít số lượng nhưng đóng góp đáng kể vào doanh thu, cần được ưu tiên trong chiến lược marketing.

Các bước tiếp theo:
- Tăng độ sâu phân tích với nhiều clusters
- Tích hợp machine learning tiên tiến hơn
- Triển khai hệ thống khuyến nghị thời gian thực