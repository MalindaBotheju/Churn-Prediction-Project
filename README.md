# 📉 Telco Customer Churn Predictor

## 📌 Project Overview
This project is an end-to-end Machine Learning pipeline that predicts whether a telecom customer will cancel their service (churn). It includes data cleaning, feature engineering, handling imbalanced data (SMOTE), model training (Logistic Regression), and a fully deployed FastAPI web interface.

## 🚀 The Web Application
The model is wrapped in a blazing-fast **FastAPI** backend with a modern **Tailwind CSS** frontend. 
Users can input customer details (Tenure, Charges, Internet Service Type, etc.) and instantly receive a Churn Probability percentage.

## 📊 Business Insights
Based on the model's feature importance analysis:
* **Top Drivers of Churn:** Month-to-month contracts, Fiber Optic internet, and lack of Tech Support.
* **Top Drivers of Retention:** Two-year contracts and having a longer tenure.

## 🛠️ Tech Stack
* **Machine Learning:** Scikit-Learn, Pandas, Imbalanced-Learn (SMOTE)
* **Backend:** FastAPI, Uvicorn, Python
* **Frontend:** HTML, Tailwind CSS, Jinja2