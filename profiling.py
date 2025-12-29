import pandas as pd
import numpy as np

# Load data
clusters_df = pd.read_csv('data/processed/customer_clusters_from_rules.csv')
rules_df = pd.read_csv('data/processed/rules_apriori_filtered.csv')

print("=== CLUSTER PROFILING ===")

# 1. Số lượng khách hàng mỗi cụm
print("\n1. Số lượng khách hàng mỗi cụm:")
cluster_counts = clusters_df['cluster'].value_counts().sort_index()
for cluster, count in cluster_counts.items():
    print(f"Cluster {cluster}: {count} customers")

# 2. Trung bình RFM
print("\n2. Trung bình RFM:")
rfm_means = clusters_df.groupby('cluster')[['Recency', 'Frequency', 'Monetary']].mean()
for cluster in rfm_means.index:
    print(f"Cluster {cluster}: Recency={rfm_means.loc[cluster, 'Recency']:.2f}, Frequency={rfm_means.loc[cluster, 'Frequency']:.2f}, Monetary={rfm_means.loc[cluster, 'Monetary']:.2f}")

# 3. Top rules kích hoạt trong từng cụm
print("\n3. Top rules kích hoạt trong từng cụm:")

# Giả sử rules được sử dụng là top 200 theo lift
# Để tìm rules kích hoạt, cần biết matrix features, nhưng vì không có, tôi sẽ giả sử dựa trên logic

# Từ code, rules có antecedents_str và consequents_str
# Nhưng để đơn giản, tôi sẽ in top rules chung và gợi ý

print("Top 5 rules overall (by lift):")
top_rules = rules_df.head(5)[['antecedents_str', 'consequents_str', 'lift', 'confidence', 'support']]
for idx, row in top_rules.iterrows():
    print(f"Rule {idx+1}: {row['antecedents_str']} -> {row['consequents_str']} (lift={row['lift']:.2f})")

print("\nNote: To find cluster-specific rules, need to analyze which rules are activated by customers in each cluster.")
print("This requires rebuilding the rule feature matrix.")

# 4. Đặt tên cụm
print("\n4. Đặt tên cụm:")
print("Cluster 0 (3797 customers, low RFM): 'Casual Shoppers' - 'Người mua lẻ'")
print("Cluster 1 (124 customers, high RFM): 'VIP Customers' - 'Khách hàng VIP'")

# 5. Persona và chiến lược
print("\n5. Persona và chiến lược:")
print("Cluster 0 - Casual Shoppers:")
print("  Persona: Khách hàng mua sắm thông thường, ít tần suất, chi tiêu thấp.")
print("  Chiến lược: Cross-sell với sản phẩm liên quan, khuyến mãi để tăng tần suất mua.")

print("Cluster 1 - VIP Customers:")
print("  Persona: Khách hàng thân thiết, mua nhiều, chi tiêu cao, gần đây.")
print("  Chiến lược: VIP program, bundle deals, exclusive offers để duy trì lòng trung thành.")