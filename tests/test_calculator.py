import pytest
import requests
from fastapi.testclient import TestClient
from ..main import app


import json

FEE_URL = "http://localhost:8000/delivery_fee"
ROOT_URL = "http://localhost:8000"

client = TestClient(app)


def test_read_root():
	response = client.get("/")
	assert response.status_code == 200
	assert response.json() == {"root": "root"}

# def test_landing_page_status():
# 	response = requests.get(ROOT_URL)
# 	assert response.status_code == 200
	
# def test_landing_page_content():
# 	expected = {"root":"root"}
# 	response = requests.get(ROOT_URL)
# 	assert response.json() == expected

# def test_delivery_fee_endpoint():
# 	payload = {
# 		"cart_value": 0,
# 		"delivery_distance": 1500,
# 		"number_of_items": 0,
# 		"time": "string"

# 	}

# 	response = requests.post(FEE_URL, payload)
# 	assert response.status_code == 200
