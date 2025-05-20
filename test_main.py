from fastapi.testclient import TestClient
from main import app  # Make sure the file is named main.py or adjust the import accordingly

client = TestClient(app)

def test_home():
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Prediction API"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_prediction():
    sample_input = {
        "CreditScore": 650,
        "Geography": "France",
        "Gender": "Female",
        "Age": 40,
        "Tenure": 5,
        "Balance": 50000.0,
        "NumOfProducts": 2,
        "HasCrCard": 1,
        "IsActiveMember": 1,
        "EstimatedSalary": 60000.0
    }
    response = client.post("/predict", json=sample_input)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert isinstance(response.json()["prediction"], int)


if __name__ == "__main__":
    test_home()
    test_health_check()
    test_prediction()