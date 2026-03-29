import os
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from app import app, db, PredictionResult  # Replace with your actual names!

# This setup allows us to test without needing a live DB connection
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use SQLite for testing
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # If your app needs to mock the DB, do it here
            db.session = UnifiedAlchemyMagicMock() 
        yield client

def test_homepage_loads(client):
    """Test that the homepage HTML is visible."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Customer Churn Predictor' in rv.data

def test_prediction_endpoint(client):
    """Test the prediction logic with sample data."""
    # Example input matching image_0.png
    sample_data = {
        "tenure": 34.0,
        "monthly_charges": 56.95,
        "contract_type": "One year",
        "internet_service": "DSL",
        "tech_support": "No",
        "online_security": "Yes",
        "paperless_billing": "No"
    }
    
    rv = client.post('/predict', data=sample_data)  # Adjust to your actual endpoint/data format
    assert rv.status_code == 200
    # Add assertions to check if model outputs predictions