import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Carbon Footprint Tracker API"

def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_activities():
    """Test getting all activities"""
    response = client.get("/api/emissions/activities")
    assert response.status_code == 200
    data = response.json()
    assert "transport" in data
    assert "energy" in data
    assert "food" in data
    assert "household" in data

def test_get_categories():
    """Test getting activity categories"""
    response = client.get("/api/emissions/categories")
    assert response.status_code == 200
    data = response.json()
    assert "categories" in data
    assert isinstance(data["categories"], list)

def test_calculate_emissions():
    """Test emissions calculation"""
    request_data = {
        "activity_type": "car_gasoline",
        "quantity": 10.0
    }
    response = client.post("/api/emissions/calculate", json=request_data)
    assert response.status_code == 200
    data = response.json()
    assert data["activity_type"] == "car_gasoline"
    assert data["quantity"] == 10.0
    assert data["co2_emissions"] == 2.1  # 0.21 * 10
    assert "kg CO₂/km" in data["unit"]

def test_calculate_emissions_invalid_activity():
    """Test emissions calculation with invalid activity"""
    request_data = {
        "activity_type": "invalid_activity",
        "quantity": 10.0
    }
    response = client.post("/api/emissions/calculate", json=request_data)
    assert response.status_code == 400
    assert "Activity type 'invalid_activity' not found" in response.json()["detail"]

def test_subscribe_user():
    """Test user subscription"""
    request_data = {
        "email": "test@example.com",
        "is_subscribed": True
    }
    response = client.post("/api/users/subscribe", json=request_data)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["is_subscribed"] == True