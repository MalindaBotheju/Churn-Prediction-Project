from fastapi.testclient import TestClient
from app import app  # Assuming your FastAPI instance is named 'app' inside 'app.py'

# Create a test client using FastAPI's built-in tool
client = TestClient(app)

def test_root_endpoint():
    """Test that the main application loads successfully."""
    response = client.get("/")
    # Even if your root route returns a 404, we just want to know the app didn't crash
    assert response.status_code in [200, 404]