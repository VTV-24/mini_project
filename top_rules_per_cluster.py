import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import sys
import os

# Add src to path
sys.path.append('src')
from cluster_library import RuleBasedCustomerClusterer

# Load data
print("Loading data...")
df_clean = pd.read_csv('data/processed/cleaned_uk_data.csv')
rules_df = pd.read_csv('data/processed/rules_apriori_filtered.csv')
clusters_df = pd.read_csv('data/processed/customer_clusters_from_rules.csv')

# Initialize clusterer
clusterer = RuleBasedCustomerClusterer(df_clean)

# Build matrices
print("Building matrices...")
clusterer.build_customer_item_matrix()
clusterer.load_rules('data/processed/rules_apriori_filtered.csv', top_k=200, sort_by='lift')

# Build features
X, meta = clusterer.build_final_features(weighting='lift', use_rfm=True, rfm_scale=True, rule_scale=False)

# Fit KMeans (assuming same as before)
labels = clusterer.fit_kmeans(X, n_clusters=2)

# Now, find top rules per cluster
print("\nTop rules activated per cluster:")

# Rule feature matrix (without RFM)
X_rules = clusterer.build_rule_feature_matrix(weighting='lift')

# For each cluster, find rules with highest activation rate
for cluster_id in [0, 1]:
    cluster_customers = labels == cluster_id
    activation_rates = X_rules[cluster_customers].mean(axis=0)  # mean activation per rule

    # Get top 5 rules
    top_indices = np.argsort(activation_rates)[::-1][:5]
    print(f"\nCluster {cluster_id} top rules:")
    for i, idx in enumerate(top_indices):
        rule = clusterer.rules_df_.iloc[idx]
        rate = activation_rates[idx]
        print(f"  {i+1}. {rule['antecedents_str']} -> {rule['consequents_str']} (activation: {rate:.3f})")