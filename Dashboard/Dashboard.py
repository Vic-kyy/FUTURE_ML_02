import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------- PAGE CONFIG (MUST BE FIRST) ----------------
st.set_page_config(page_title="Churn Risk Dashboard", layout="wide")

st.title("📊 Customer Churn Risk Dashboard")

# ---------------- LOAD DATA ----------------
DATA_PATH = "/Users/vic/Desktop/Churn Prediction/Data/risk_output.csv"

if not os.path.exists(DATA_PATH):
    st.error("risk_output.csv not found. Please generate it from the notebook.")
    st.stop()

risk_df = pd.read_csv(DATA_PATH)

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("🔎 Filters")

risk_filter = st.sidebar.multiselect(
    "Select Risk Level",
    options=risk_df['Risk_Level'].unique(),
    default=risk_df['Risk_Level'].unique()
)

tenure_min, tenure_max = st.sidebar.slider(
    "Tenure (months)",
    int(risk_df['tenure'].min()),
    int(risk_df['tenure'].max()),
    (int(risk_df['tenure'].min()), int(risk_df['tenure'].max()))
)

# ---------------- APPLY FILTERS ----------------
filtered_df = risk_df[
    (risk_df['Risk_Level'].isin(risk_filter)) &
    (risk_df['tenure'] >= tenure_min) &
    (risk_df['tenure'] <= tenure_max)
]

# ---------------- KPIs ----------------
total_customers = len(filtered_df)
churn_rate = filtered_df['Actual_Churn'].mean() * 100 if total_customers else 0
high_risk_pct = (filtered_df['Risk_Level'] == 'High Risk').mean() * 100 if total_customers else 0

col1, col2, col3 = st.columns(3)
col1.metric("Customers", total_customers)
col2.metric("Churn Rate (%)", f"{churn_rate:.1f}")
col3.metric("High Risk (%)", f"{high_risk_pct:.1f}")

# ---------------- SIDE-BY-SIDE PLOTS ----------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔍 Churn Risk Distribution")
    fig, ax = plt.subplots(figsize=(4, 3))
    filtered_df['Risk_Level'].value_counts().plot(kind='bar', ax=ax)
    ax.set_xlabel("Risk Level")
    ax.set_ylabel("Customers")
    st.pyplot(fig)

with col2:
    st.subheader("📈 Churn Probability Distribution")
    fig2, ax2 = plt.subplots(figsize=(4, 3))
    ax2.hist(filtered_df['Churn_Probability'], bins=20)
    ax2.set_xlabel("Churn Probability")
    ax2.set_ylabel("Customers")
    st.pyplot(fig2)

# ---------------- HIGH RISK TABLE ----------------
st.subheader("🚨 High Risk Customers")

high_risk_df = filtered_df[filtered_df['Risk_Level'] == 'High Risk']
st.dataframe(high_risk_df.head(20), use_container_width=True)

# ---------------- DYNAMIC BUSINESS INSIGHTS ----------------
st.divider()
st.subheader("💡 Dynamic Business Insights")

if total_customers == 0:
    st.warning("No customers match the selected filters.")
else:
    churned = filtered_df['Actual_Churn'].sum()
    high_risk_churn_rate = (
        high_risk_df['Actual_Churn'].mean() * 100
        if len(high_risk_df) > 0 else 0
    )

    st.markdown(f"""
    **Insights based on current filters:**

    • Total customers analyzed: **{total_customers}**  
    • Customers churned: **{int(churned)}**  
    • Overall churn rate: **{churn_rate:.1f}%**  
    • High-risk customer churn rate: **{high_risk_churn_rate:.1f}%**

    **Recommendations:**
    - Prioritize **High-Risk customers** for retention campaigns  
    - Focus on customers with **shorter tenure**  
    - Trigger proactive outreach for churn probability > **0.6**
    """)