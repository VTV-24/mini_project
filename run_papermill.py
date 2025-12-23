import papermill as pm
import os

os.makedirs("notebooks/runs", exist_ok=True)

# ==============================
# 1. PREPROCESSING + EDA
# ==============================
pm.execute_notebook(
    "notebooks/preprocessing_and_eda.ipynb",
    "notebooks/runs/preprocessing_and_eda_run.ipynb",
    parameters=dict(
        DATA_PATH="data/raw/online_retail.csv",
        COUNTRY="United Kingdom",
        OUTPUT_DIR="data/processed",
        PLOT_REVENUE=False,
        PLOT_TIME_PATTERNS=False,
        PLOT_PRODUCTS=False,
        PLOT_CUSTOMERS=False,
        PLOT_RFM=False,
    ),
    kernel_name="python3",
)

# ==============================
# 2. BASKET PREPARATION
# ==============================
pm.execute_notebook(
    "notebooks/basket_preparation.ipynb",
    "notebooks/runs/basket_preparation_run.ipynb",
    parameters=dict(
        CLEANED_DATA_PATH="data/processed/cleaned_uk_data.csv",
        BASKET_BOOL_PATH="data/processed/basket_bool.parquet",
        INVOICE_COL="InvoiceNo",
        ITEM_COL="Description",
        QUANTITY_COL="Quantity",
        THRESHOLD=1,
    ),
    kernel_name="python3",
)

# ==============================
# 3. FP-GROWTH MODELLING (THAY APRIORI)
# ==============================
pm.execute_notebook(
    "notebooks/fp_growth_modelling.ipynb",
    "notebooks/runs/fp_growth_modelling_run.ipynb",
    parameters=dict(
        BASKET_BOOL_PATH="data/processed/basket_bool.parquet",
        RULES_OUTPUT_PATH="data/processed/rules_fpgrowth_filtered.csv",

        # Tham số FP-Growth (an toàn RAM)
        MIN_SUPPORT=0.03,
        MAX_LEN=3,

        METRIC="lift",
        MIN_THRESHOLD=1.0,

        FILTER_MIN_SUPPORT=0.03,
        FILTER_MIN_CONF=0.3,
        FILTER_MIN_LIFT=1.2,
        FILTER_MAX_ANTECEDENTS=2,
        FILTER_MAX_CONSEQUENTS=1,

        TOP_N_RULES=20,

        # Tắt plot khi chạy batch
        PLOT_TOP_LIFT=False,
        PLOT_TOP_CONF=False,
        PLOT_SCATTER=False,
        PLOT_NETWORK=False,
        PLOT_PLOTLY_SCATTER=False,
    ),
    kernel_name="python3",
)

# ==============================
# 4. CLUSTERING FROM RULES (DÙNG RULE FP-GROWTH)
# ==============================
pm.execute_notebook(
    "notebooks/clustering_from_rules.ipynb",
    "notebooks/runs/clustering_from_rules_run.ipynb",
    parameters=dict(
        CLEANED_DATA_PATH="data/processed/cleaned_uk_data.csv",
        RULES_INPUT_PATH="data/processed/rules_fpgrowth_filtered.csv",

        TOP_K_RULES=200,
        SORT_RULES_BY="lift",
        WEIGHTING="lift",
        MIN_ANTECEDENT_LEN=1,
        USE_RFM=True,
        RFM_SCALE=True,
        RULE_SCALE=False,

        K_MIN=2,
        K_MAX=10,
        N_CLUSTERS=None,
        RANDOM_STATE=42,

        OUTPUT_CLUSTER_PATH="data/processed/customer_clusters_from_rules.csv",

        PROJECTION_METHOD="pca",
        PLOT_2D=True,
    ),
    kernel_name="python3",
)

print("✅ Đã chạy xong pipeline với FP-Growth")
