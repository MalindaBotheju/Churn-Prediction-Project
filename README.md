# 📉 Telco Customer Churn Predictor AI

[![Live Demo](https://img.shields.io/badge/LIVE%20DEMO-CLICK%20HERE-5cba36?style=for-the-badge)](https://churn-prediction-project-i7g4.onrender.com/)

---

## 📌 Project Overview
This project is a fully deployed Machine Learning application that helps telecom companies identify customers who are at high risk of canceling their subscriptions. Users can input customer metrics into the modern web dashboard and instantly receive a churn probability score.

<img src="screenshots/dash.png" alt="Main Dashboard" width="600">

---

## 📸 Prediction Results

| High Risk Customer Detection | Safe Customer Detection |
| :---: | :---: |
| <img src="screenshots/risk.png" alt="High Risk" width="100%"> | <img src="screenshots/safe.png" alt="Safe" width="100%"> |

---

## 🏗️ System Architecture & MLOps
This project is built to mirror enterprise-level software standards, moving beyond a simple ML script into a fully containerized, tested, and deployed web service.

* **Machine Learning:** Imbalanced data handled via SMOTE, trained using Logistic Regression (Scikit-Learn), and serialized for production.
* **Backend API:** Built with FastAPI for high-performance, asynchronous request handling.
* **Database:** Production predictions are securely logged to a cloud-hosted PostgreSQL database for future model retraining and monitoring.
* **Containerization:** Fully containerized using Docker (Python 3.12-slim base) for consistent environments across development and production.
* **CI/CD Quality Gate:** Automated GitHub Actions pipeline that lints code (Flake8) and runs automated tests (Pytest) in an isolated in-memory SQLite database before allowing deployments.

---

## 📊 Business Insights & ML Performance
Based on the model's feature importance analysis, we discovered exactly what drives customer behavior:
* **Top Drivers of Churn:** Month-to-month contracts, Fiber Optic internet, and lack of Tech Support.
* **Top Drivers of Retention:** Two-year contracts, longer tenure, and having supplementary security services.
* **Model Performance:** Achieved an 79% accuracy rate and a 0.71 F1-score on the testing holdout set.

---

## 🧪 Test it Yourself!
Want to test the live model? Try inputting these two customer profiles straight into the web app:

**Profile 1: Likely to Churn (High Risk Customer)**
* **Tenure:** 2 months | **Contract:** Month-to-month | **Internet:** Fiber Optic
* **Tech Support:** No | **Online Security:** No | **Monthly Charges:** $70.70

**Profile 2: Likely to Stay (Safe Customer)**
* **Tenure:** 72 months | **Contract:** Two year | **Internet:** DSL
* **Tech Support:** Yes | **Online Security:** Yes | **Monthly Charges:** $90.25

---

## 🚀 How to Run Locally

### Prerequisites
Before you begin, ensure you have the following installed:
* **Git:** To clone the repository.
* **Docker:** For running the application in an isolated, 100% reproducible environment.

---

**1. Clone the repository:**
```bash
git clone https://github.com/MalindaBotheju/Churn-Prediction-Project.git
```
```bash
cd Churn-Prediction-Project
```

**2. Set up your Environment Variables:**

Create a .env file in the root directory and add your database URL (or use a local SQLite database for testing):

Code snippet
```bash
DATABASE_URL=sqlite:///./test.db
```

**3. Build and Run with Docker:**
```bash
docker build -t churn-api .
```
```bash
docker run -p 8000:8000 --env-file .env churn-api
```

**4. View the Application**

Frontend Web UI: Open http://localhost:8000

API Documentation: Open http://localhost:8000/docs

Developed by Malinda Boteju