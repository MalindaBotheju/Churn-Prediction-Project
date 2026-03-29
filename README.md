# 📉 Telco Customer Churn Predictor AI

[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql)](https://www.postgresql.org/)
[![CI/CD Pipeline](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions)](https://github.com/features/actions)

An end-to-end Machine Learning pipeline and API that predicts whether a telecom customer will cancel their service (churn). 

### 🌟 Live Links
* **Live Web App:** [[Insert your Render URL here]](https://churn-prediction-project-i7g4.onrender.com/)
* **Interactive API Documentation (Swagger):** [[Insert your Render URL here]/docs](https://churn-prediction-project-i7g4.onrender.com/docs)

*(Note: Hosted on a free Render tier. The server may take 30-50 seconds to wake up on the first load. Thank you for your patience!)*

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
* **Model Performance:** *(Add your accuracy here, e.g., Achieved an 82% accuracy rate and a 0.78 F1-score on the testing holdout set).*

---

## 🧪 Test it Yourself!
Want to test the live model? Try inputting these two vastly different customer profiles into the web app (or via the `/docs` API endpoint):

**Profile 1: Likely to Churn (High Risk)**
* **Tenure:** 2 months | **Contract:** Month-to-month | **Internet:** Fiber Optic
* **Tech Support:** No | **Online Security:** No | **Monthly Charges:** $95.50

**Profile 2: Likely to Stay (Safe)**
* **Tenure:** 68 months | **Contract:** Two year | **Internet:** DSL
* **Tech Support:** Yes | **Online Security:** Yes | **Monthly Charges:** $25.00

---

## 🚀 How to Run Locally

## Prerequisites
Before you begin, ensure you have the following installed:
* **Git:** To clone the repository.
* **Docker:** For running the application in an isolated, 100% reproducible environment.

---

**1. Clone the repository**
     ```bash
     git clone https://github.com/MalindaBotheju/Churn-Prediction-Project.git
     ```
     ```bash
     cd Churn-Prediction-Project
     ```

**2. Set up your Environment Variables**
    Create a .env file in the root directory and add your database URL (or use a local SQLite database for testing):

    Code snippet
    DATABASE_URL=sqlite:///./test.db

**3. Build and Run with Docker**
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