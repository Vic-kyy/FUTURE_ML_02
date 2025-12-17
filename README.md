📊 Customer Churn Prediction & Risk Analysis Dashboard

🔍 Project Overview

Customer churn is a critical business problem where retaining existing customers is far more cost-effective than acquiring new ones.
This project builds an end-to-end churn prediction system that not only predicts churn but also segments customers by risk level and presents actionable business insights through an interactive Streamlit dashboard.

The solution combines machine learning, probability-based risk segmentation, and business-focused visualization to support real-world decision making.

🎯 Objectives
	•	Predict the probability of customer churn using historical customer data
	•	Identify key churn drivers affecting customer retention
	•	Segment customers into Low / Medium / High churn risk categories
	•	Enable business teams to prioritize retention strategies
	•	Present insights via an interactive Streamlit dashboard

🧠 Machine Learning Approach

Models Used
	•	Logistic Regression (Baseline & Final Model)
	•	Random Forest (comparison)
	•	XGBoost (comparison)

Why Logistic Regression?
	•	Achieved the best ROC-AUC score
	•	Highly interpretable for business stakeholders
	•	Enabled clear identification of churn drivers
	•	Improved recall through threshold tuning

📈 Model Evaluation

Key evaluation techniques:
	•	Confusion Matrix
	•	Precision, Recall, F1-score
	•	ROC-AUC
	•	Threshold tuning for business optimization

Threshold Optimization

Instead of using the default threshold (0.5), the model was tuned to 0.4, resulting in:
	•	Higher churn recall
	•	Fewer missed churners
	•	Balanced false positives
  
🚦 Churn Risk Segmentation

Customers are segmented based on churn probability:

Risk Level	Churn Probability	Business Action
🟢 Low Risk	0.0 – 0.3	No action
🟡 Medium Risk	0.3 – 0.6	Email / reminder
🔴 High Risk	0.6 – 1.0	Call / discount

This enables risk-based retention strategies instead of binary predictions.

📊 Streamlit Dashboard Features
	•	📌 KPI Metrics (Customers, Churn Rate, High-Risk %)
	•	🔎 Dynamic Filters (Risk Level, Tenure)
	•	📊 Side-by-side visualizations
	•	🚨 High-Risk Customer Table
	•	💡 Dynamic Business Insights that update with filters

💡 Key Business Insights

🔴 Churn Drivers
	•	Month-to-month contracts show higher churn
	•	Electronic check payment users churn more
	•	High monthly charges increase churn risk
	•	Lack of tech support or online security raises churn probability

🟢 Retention Drivers
	•	Long-term contracts (1–2 years) significantly reduce churn
	•	Support services improve customer loyalty
	•	Longer tenure correlates with lower churn

🛠️ Tech Stack
	•	Python
	•	Pandas, NumPy
	•	Scikit-learn
	•	XGBoost
	•	Matplotlib
	•	Streamlit
	•	Git & GitHub


🎓 What I Learned
	•	Handling imbalanced classification problems
	•	Evaluating models beyond accuracy
	•	Threshold tuning for business impact
	•	Translating ML outputs into actionable insights
	•	Building interactive dashboards for decision-makers

⸻

📌 Future Improvements
	•	Real-time prediction using user input
	•	Model selection toggle in dashboard
	•	Deployment on Streamlit Cloud
	•	Automated retraining pipeline

<img width="1454" height="807" alt="Screenshot 2025-12-17 at 6 46 38 PM" src="https://github.com/user-attachments/assets/3ad153fb-cbf1-4a2d-8b24-8a975e14f540" />
<img width="1380" height="519" alt="Screenshot 2025-12-17 at 6 46 59 PM" src="https://github.com/user-attachments/assets/908bd7aa-9e2e-4f74-9f4b-dfeb41ec7f14" />
<img width="1423" height="483" alt="Screenshot 2025-12-17 at 6 47 12 PM" src="https://github.com/user-attachments/assets/b0cafc8d-3ff9-41c8-8d74-7da82b743cd8" />
