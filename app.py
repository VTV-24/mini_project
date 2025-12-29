import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Load data
@st.cache_data
def load_data():
    clusters_df = pd.read_csv('data/processed/customer_clusters_from_rules.csv')
    rules_df = pd.read_csv('data/processed/rules_apriori_filtered.csv')
    top_rules_df = pd.read_csv('data/processed/top_rules_per_cluster.csv')
    return clusters_df, rules_df, top_rules_df

clusters_df, rules_df, top_rules_df = load_data()

# Title
st.title("Customer Segmentation Dashboard")
st.markdown("Phân tích cụm khách hàng dựa trên luật kết hợp (Association Rules)")

# Sidebar
st.sidebar.header("Filters")
selected_cluster = st.sidebar.selectbox("Chọn cụm khách hàng:", [0, 1])

# Filter data
filtered_df = clusters_df[clusters_df['cluster'] == selected_cluster]

# Cluster info
st.header(f"Thông tin cụm {selected_cluster}")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Số khách hàng", len(filtered_df))
with col2:
    st.metric("Recency trung bình", f"{filtered_df['Recency'].mean():.1f}")
with col3:
    st.metric("Monetary trung bình", f"{filtered_df['Monetary'].mean():.1f}")

# RFM Distribution
st.subheader("Phân bố RFM")
fig_rfm = px.histogram(filtered_df, x="Recency", nbins=20, title="Recency Distribution")
st.plotly_chart(fig_rfm)

# Top Rules
st.subheader("Top Rules theo cụm")
filtered_top_rules = top_rules_df[top_rules_df['cluster'] == selected_cluster].sort_values('rank')
st.dataframe(filtered_top_rules[['rank', 'rule', 'activation_rate']].rename(columns={
    'rank': 'Thứ hạng',
    'rule': 'Luật',
    'activation_rate': 'Tỷ lệ kích hoạt'
}))

# Persona and Strategy
st.header("Persona và Chiến lược")
if selected_cluster == 0:
    st.write("**Persona:** Khách hàng mua sắm thông thường, ít tần suất, chi tiêu thấp.")
    st.write("**Chiến lược:** Cross-sell với sản phẩm liên quan, khuyến mãi để tăng tần suất mua.")
elif selected_cluster == 1:
    st.write("**Persona:** Khách hàng thân thiết, mua nhiều, chi tiêu cao, gần đây.")
    st.write("**Chiến lược:** VIP program, bundle deals, exclusive offers để duy trì lòng trung thành.")

# Bundle Suggestions
st.subheader("Gợi ý Bundle/Cross-sell")
if selected_cluster == 0:
    top_rule = filtered_top_rules.iloc[0]['rule'] if len(filtered_top_rules) > 0 else "Không có luật"
    st.write(f"**Gợi ý dựa trên luật hàng đầu:** {top_rule}")
    st.write("**Chiến lược:** Cross-sell với sản phẩm liên quan như Scandinavian Christmas decorations.")
elif selected_cluster == 1:
    top_rule = filtered_top_rules.iloc[0]['rule'] if len(filtered_top_rules) > 0 else "Không có luật"
    st.write(f"**Gợi ý dựa trên luật hàng đầu:** {top_rule}")
    st.write("**Chiến lược:** Bundle deals với herb markers và sản phẩm liên quan.")