import pytest
from unittest.mock import patch
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_calculate_called_on_invalid_date(client):
    with patch('calculate_expiry.calculate_expiry_date') as mock_calculate:
        mock_calculate.return_value = "2026-03-26"

        response = client.post('/calculate_expiry', json={
            "expiryDate": "invalid-date"
        })

        mock_calculate.assert_called_once()

        assert response.status_code == 200
        data = response.get_json()
        assert data["estimatedExpiryDate"] == "2026-03-26"
        assert "Expiry date was missing or invalid" in data["message"]

def test_returns_estimated_expiry_date(client):
    with patch('calculate_expiry.calculate_expiry_date') as mock_calculate:
        mock_calculate.return_value = "2026-03-26"

        response = client.post('/calculate_expiry', json={})
        data = response.get_json()

        assert response.status_code == 200
        assert "estimatedExpiryDate" in data
        assert data["estimatedExpiryDate"] == "2026-03-26"
        assert "Expiry date was missing or invalid" in data["message"]

        response2 = client.post('/calculate_expiry', json={"expiryDate": "abc"})
        data2 = response2.get_json()

        assert response2.status_code == 200
        assert "estimatedExpiryDate" in data2
        assert data2["estimatedExpiryDate"] == "2026-03-26"
        assert "Expiry date was missing or invalid" in data2["message"]

        response3 = client.post('/calculate_expiry', json={"expiryDate": "2026-13-40"})
        data3 = response3.get_json()

        assert response3.status_code == 200
        assert "estimatedExpiryDate" in data3
        assert data3["estimatedExpiryDate"] == "2026-03-26"
        assert "Expiry date was missing or invalid" in data3["message"]

def test_valid_date_does_not_trigger_calculator(client):
    with patch('calculate_expiry.calculate_expiry_date') as mock_calculate:
        response = client.post('/calculate_expiry', json={"expiryDate": "2026-03-25"})

        mock_calculate.assert_not_called()

        data = response.get_json()
        assert response.status_code == 200
        assert data["expiryDate"] == "2026-03-25"
        assert "Expiry date provided" in data["message"]