import pandas as pd
import numpy as np
import sys
import os

# Add src to path
sys.path.append('src')

from cluster_library import RuleBasedCustomerClusterer

# Load data
df_clean = pd.read_csv('data/processed/cleaned_uk_data.csv')
rules_df = pd.read_csv('data/processed/rules_apriori_filtered.csv')

# Build clusterer
clusterer = RuleBasedCustomerClusterer(df_clean)
clusterer.load_rules('data/processed/rules_apriori_filtered.csv', top_k=200, sort_by='lift')

# Build features
X, meta = clusterer.build_final_features(weighting='lift', use_rfm=True, rfm_scale=True, rule_scale=False)

# Fit KMeans (assuming same as before)
labels = clusterer.fit_kmeans(X, n_clusters=2)

# Rule feature matrix (without RFM)
X_rules = clusterer.build_rule_feature_matrix(weighting='lift')

# For each cluster, find rules with highest activation rate
top_rules_data = []
for cluster_id in [0, 1]:
    cluster_customers = labels == cluster_id
    activation_rates = X_rules[cluster_customers].mean(axis=0)  # mean activation per rule

    # Get top 5 rules
    top_indices = np.argsort(activation_rates)[::-1][:5]
    for rank, idx in enumerate(top_indices, 1):
        rule = clusterer.rules_df_.iloc[idx]
        rule_str = f"{rule['antecedents_str']} -> {rule['consequents_str']}"
        rate = activation_rates[idx]
        top_rules_data.append({
            'cluster': cluster_id,
            'rank': rank,
            'rule': rule_str,
            'activation_rate': rate
        })

# Create dataframe
top_rules_df = pd.DataFrame(top_rules_data)

top_rules_df.to_csv('data/processed/top_rules_per_cluster.csv', index=False)
print('Top rules per cluster saved to data/processed/top_rules_per_cluster.csv')