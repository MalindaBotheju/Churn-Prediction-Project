# Telco Customer Churn Dataset

## Overview
This dataset contains customer information for a telecommunications company. The primary objective is to predict customer churn—whether a customer will stop doing business with the company—based on their demographics, subscribed services, and account information. 

## Dataset Features
The dataset consists of 21 columns:

**Customer Demographics:**
* `customerID`: Unique identifier for each customer.
* `gender`: The gender of the customer (Male/Female).
* `SeniorCitizen`: Indicates if the customer is a senior citizen (1, 0).
* `Partner`: Indicates if the customer has a partner (Yes, No).
* `Dependents`: Indicates if the customer has dependents (Yes, No).

**Services Subscribed:**
* `PhoneService`: Indicates if the customer has a phone service (Yes, No).
* `MultipleLines`: Indicates if the customer has multiple lines (Yes, No, No phone service).
* `InternetService`: Customer's internet service provider (DSL, Fiber optic, No).
* `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies`: Indicates if the customer has these respective additional services (Yes, No, No internet service).

**Account Information:**
* `tenure`: Number of months the customer has stayed with the company.
* `Contract`: The contract term of the customer (Month-to-month, One year, Two year).
* `PaperlessBilling`: Indicates if the customer has paperless billing (Yes, No).
* `PaymentMethod`: The customer's payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic)).
* `MonthlyCharges`: The amount charged to the customer monthly.
* `TotalCharges`: The total amount charged to the customer.

**Target Variable:**
* `Churn`: Whether the customer churned or not (Yes or No).
