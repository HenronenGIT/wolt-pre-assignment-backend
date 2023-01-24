import requests
import json
from .utils import *

FEE_URL = "http://localhost:8000/delivery_fee"
ROOT_URL = "http://localhost:8000"

# def test_landing_page_status():
# 	response = requests.get(ROOT_URL)
# 	assert response.status_code == 200

# def test_landing_page_content():
# 	expected = {"root": "root"}
# 	response = requests.get(ROOT_URL)
# 	assert response.json() == expected

def test_free_delivery():
	cart = {
		"cart_value": 10000,
		"delivery_distance": 0,
		"number_of_items": 0,
		"time": "2021-10-12T13:00:00Z"
	}
	status_code = get_delivery_fee_status(cart)
	content = get_delivery_fee_content(cart)
	assert status_code == 200
	assert content == {"delivery_fee": 0}

# def test_free_delivery():
# 	cart = {
# 		"cart_value": 10000,
# 		"delivery_distance": 0,
# 		"number_of_items": 0,
# 		"time": "2021-10-12T13:00:00Z"
# 	}
# 	content = get_delivery_fee_content(cart)
# 	assert content == {'delivery_fee': 0}

# def test_max_delivery_fee():
# 	cart = {
# 		"cart_value": 0,
# 		"delivery_distance": 0,
# 		"number_of_items": 0,
# 		"time": "2023-10-12T13:00:00Z"
# 	}
# 	content = get_delivery_fee_content(cart)
# 	assert content == {'delivery_fee': 0}
# 	cart['cart_value'] = 101
# 	content = get_delivery_fee_content(cart)
# 	assert content == {'delivery_fee': 0}
# 	cart['cart_value'] = 10000
# 	content = get_delivery_fee_content(cart)
# 	assert content == {'delivery_fee': 0}

# def test_rush_hour_fee():
# 	cart = {
# 		"cart_value": 100,
# 		"delivery_distance": 0,
# 		"number_of_items": 0,
# 		"time": "2023-1-20T17:00:00Z"
# 	}
# 	content = get_delivery_fee_content(cart)
# 	assert content == {'delivery_fee': 0}

