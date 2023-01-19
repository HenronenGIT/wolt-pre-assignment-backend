import requests
import json

# Run from the terminal with pytest

FEE_URL = "http://localhost:8000/delivery_fee"
ROOT_URL = "http://localhost:8000"

def get_delivery_fee(cart: dict):
	response = requests.get(FEE_URL, json = cart)
	return response

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

# def test_delivery_fee_return_value():
# 	cart = {
# 		"cart_value": 890,
# 		"delivery_distance": 1500,
# 		"number_of_items": 0,
# 		"time": "string"
# 	}
# 	response = requests.get(FEE_URL, json = cart)
# 	data = json.loads(response.content)
# 	assert data == {'delivery_fee': 300}

def test_item_count_calculations():
	cart = {
		"cart_value": 0,
		"delivery_distance": 0,
		"number_of_items": 1,
		"time": "string"
	}
	response = get_delivery_fee(cart)
	assert response.status_code == 200
	response = get_delivery_fee(cart)
	data = json.loads(response.content)
	assert data == {'delivery_fee': 0}
	cart['number_of_items'] = 5
	response = get_delivery_fee(cart)
	assert json.loads(response.content) == {'delivery_fee': 50}
	cart['number_of_items'] = 10
	response = get_delivery_fee(cart)
	assert json.loads(response.content) == {'delivery_fee': 300}
	cart['number_of_items'] = 12
	response = get_delivery_fee(cart)
	assert json.loads(response.content) == {'delivery_fee': 400}


