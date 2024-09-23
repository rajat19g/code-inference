import pytest
from pathlib import Path
from fastapi.testclient import TestClient
from demo_inference.app import app
import json


client = TestClient(app)

current_file = Path(__file__).resolve()
data_dir = current_file.parent / 'test_data'

# Full path to the JSON file
json_file_path = data_dir / 'requests.json'

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict():
 
    with open(json_file_path, "r") as f:
        json_request_mock = json.load(f)
    response = client.post("/predict", json=json_request_mock)
    assert response.status_code == 200
    assert response.json() == {"prediction": 1}