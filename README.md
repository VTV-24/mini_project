# Customer Segmentation using Association Rules

Dự án phân tích dữ liệu mining sử dụng luật kết hợp (Association Rules) để phân cụm khách hàng và phát triển chiến lược marketing.

## Tổng quan

Dự án này áp dụng kỹ thuật data mining để:
- Khám phá luật kết hợp từ dữ liệu giao dịch
- Sử dụng luật kết hợp làm đặc trưng để phân cụm khách hàng
- Phát triển chiến lược marketing dựa trên phân tích cụm

## Cấu trúc dự án

```
├── data/
│   ├── raw/
│   │   └── online_retail.csv          # Dữ liệu gốc
│   └── processed/
│       ├── cleaned_uk_data.csv        # Dữ liệu đã làm sạch
│       ├── rules_apriori_filtered.csv # Luật kết hợp từ Apriori
│       ├── customer_clusters_from_rules.csv # Kết quả phân cụm
│       └── top_rules_per_cluster.csv  # Top rules per cluster
├── notebooks/
│   ├── preprocessing_and_eda.ipynb    # EDA và tiền xử lý
│   ├── basket_preparation.ipynb       # Chuẩn bị dữ liệu giỏ hàng
│   ├── apriori_modelling.ipynb        # Mô hình Apriori
│   ├── fp_growth_modelling.ipynb      # Mô hình FP-Growth
│   ├── compare_apriori_fpgrowth.ipynb # So sánh hai thuật toán
│   └── clustering_from_rules.ipynb    # Phân cụm từ luật kết hợp
├── src/
│   └── cluster_library.py             # Thư viện phân cụm
├── app.py                             # Dashboard Streamlit
├── cluster_analysis_report.md         # Báo cáo phân tích
└── requirements.txt                   # Dependencies
```

## Cài đặt

1. Clone repository:
```bash
git clone <repository-url>
cd mini_project
```

2. Tạo virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# hoặc
source venv/bin/activate  # Linux/Mac
```

3. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

## Sử dụng

### 1. Chạy notebooks (theo thứ tự):
```bash
jupyter notebook
# Mở và chạy từng notebook theo thứ tự
```

### 2. Chạy dashboard:
```bash
streamlit run app.py
```

Dashboard sẽ chạy tại `http://localhost:8501`

### 3. Xem báo cáo:
Mở file `cluster_analysis_report.md` để xem phân tích chi tiết.

## Kết quả chính

- **2 cụm khách hàng:** Casual Shoppers (97%) và VIP Customers (3%)
- **VIP Customers** dù ít số lượng nhưng đóng góp 70% doanh thu
- **Chiến lược:** Tập trung vào retention cho VIP và reactivation cho Casual

## Tác giả

An

## License

None
