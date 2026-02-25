# app.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import pandas as pd
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load your saved brain!
model = joblib.load('telco_churn_model.pkl')
scaler = joblib.load('telco_scaler.pkl')

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "prediction": None})

@app.post("/", response_class=HTMLResponse)
async def predict(request: Request):
    form_data = await request.form()
    
    # 1. Grab ALL the data from the user interface
    tenure = float(form_data['tenure'])
    monthly_charges = float(form_data['monthly_charges'])
    contract = form_data['contract']
    internet_service = form_data['internet_service']
    tech_support = form_data['tech_support']
    online_security = form_data['online_security']
    paperless_billing = form_data['paperless_billing']
    
    # 2. Get expected columns and create a blank dataframe
    expected_columns = model.feature_names_in_
    input_dict = {col: [0] for col in expected_columns}
    input_df = pd.DataFrame(input_dict)
    
    # 3. Fill in and scale numerical data
    unscaled_df = pd.DataFrame({
        'tenure': [tenure], 
        'MonthlyCharges': [monthly_charges], 
        'TotalCharges': [tenure * monthly_charges]
    })
    scaled_values = scaler.transform(unscaled_df)
    
    input_df['tenure'] = scaled_values[0][0]
    input_df['MonthlyCharges'] = scaled_values[0][1]
    input_df['TotalCharges'] = scaled_values[0][2]
    
    # 4. ONE-HOT ENCODING TRANSLATIONS
    
    # Contract
    if contract == "One year" and 'Contract_One year' in input_df.columns:
        input_df['Contract_One year'] = 1
    elif contract == "Two year" and 'Contract_Two year' in input_df.columns:
        input_df['Contract_Two year'] = 1
        
    # Internet Service
    if internet_service == "Fiber optic" and 'InternetService_Fiber optic' in input_df.columns:
        input_df['InternetService_Fiber optic'] = 1
    elif internet_service == "No" and 'InternetService_No' in input_df.columns:
        input_df['InternetService_No'] = 1

    # Tech Support
    if tech_support == "Yes" and 'TechSupport_Yes' in input_df.columns:
        input_df['TechSupport_Yes'] = 1
    elif tech_support == "No internet service" and 'TechSupport_No internet service' in input_df.columns:
        input_df['TechSupport_No internet service'] = 1

    # Online Security
    if online_security == "Yes" and 'OnlineSecurity_Yes' in input_df.columns:
        input_df['OnlineSecurity_Yes'] = 1
    elif online_security == "No internet service" and 'OnlineSecurity_No internet service' in input_df.columns:
        input_df['OnlineSecurity_No internet service'] = 1

    # Paperless Billing (You manually mapped Yes=1, No=0 in your notebook)
    if 'PaperlessBilling' in input_df.columns:
        input_df['PaperlessBilling'] = 1 if paperless_billing == "Yes" else 0

    
    # 5. Make the Real Prediction!
    probability = model.predict_proba(input_df)[0][1]
    is_churn = probability > 0.5  
    
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "prediction": bool(is_churn),
        "probability": round(probability * 100, 1)
    })

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)