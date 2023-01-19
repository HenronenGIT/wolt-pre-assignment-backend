import pytest
import requests
from fastapi.testclient import TestClient

import json

FEE_URL = "http://localhost:8000/delivery_fee"
ROOT_URL = "http://localhost:8000"

def test_landing_page_status():
	response = requests.get(ROOT_URL)
	assert response.status_code == 200
	
def test_landing_page_content():
	expected = {"root":"root"}
	response = requests.get(ROOT_URL)
	assert response.json() == expected

def test_delivery_fee_status():
	cart = {
		"cart_value": 0,
		"delivery_distance": 1500,
		"number_of_items": 0,
		"time": "string"

	}
	response = requests.get(FEE_URL, json = cart)
	assert response.status_code == 200

def test_delivery_fee_return_value():

	cart = {
		"cart_value": 890,
		"delivery_distance": 1500,
		"number_of_items": 0,
		"time": "string"
	}
	response = requests.get(FEE_URL, json = cart)
	data = json.loads(response.content)
	assert data == {'delivery_fee': 300}
