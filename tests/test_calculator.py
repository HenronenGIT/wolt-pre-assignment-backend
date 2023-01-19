import requests
import json
from test_helpers import *

# Run from the terminal with pytest

FEE_URL = "http://localhost:8000/delivery_fee"
ROOT_URL = "http://localhost:8000"


def test_landing_page_status():
	response = requests.get(ROOT_URL)
	assert response.status_code == 200


def test_landing_page_content():
	expected = {"root": "root"}
	response = requests.get(ROOT_URL)
	assert response.json() == expected

def test_delivery_fee_status():
	cart = {
		"cart_value": 0,
		"delivery_distance": 1500,
		"number_of_items": 0,
		"time": "string"
	}
	status_code = get_delivery_fee_status(cart)
	assert status_code == 200

def test_delivery_fee_status():
	cart = {
		"cart_value": 0,
		"delivery_distance": 0,
		"number_of_items": 1,
		"time": "string"
	}
	status_code = get_delivery_fee_status(cart)
	assert status_code == get_delivery_fee_status(cart)

def test_delivery_fee_return_value():
	cart = {
		"cart_value": 0,
		"delivery_distance": 0,
		"number_of_items": 1,
		"time": "string"
	}
	content = get_delivery_fee_content(cart)
	assert content == {'delivery_fee': 0}
	cart['number_of_items'] = 5
	content = get_delivery_fee_content(cart)
	assert content == {'delivery_fee': 50}
	cart['number_of_items'] = 10
	content = get_delivery_fee_content(cart)
	assert content == {'delivery_fee': 300}
	cart['number_of_items'] = 12
	content = get_delivery_fee_content(cart)
	assert content == {'delivery_fee': 400}

def test_free_delivery_fee():
	cart = {
		"cart_value": 100,
		"delivery_distance": 0,
		"number_of_items": 0,
		"time": "string"
	}
	content = get_delivery_fee_content(cart)
	assert content == {'delivery_fee': 0}
	cart['cart_value'] = 101
	content = get_delivery_fee_content(cart)
	assert content == {'delivery_fee': 0}
	cart['cart_value'] = 10000
	content = get_delivery_fee_content(cart)
	assert content == {'delivery_fee': 0}

# def test_max_delivery_fe():
# 	cart = {
# 		"cart_value": 100,
# 		"delivery_distance": 0,
# 		"number_of_items": 0,
# 		"time": "string"
# 	}
# 	content = get_delivery_fee_content(cart)
# 	assert content == {'delivery_fee': 0}
# 	cart['cart_value'] = 101
# 	content = get_delivery_fee_content(cart)
# 	assert content == {'delivery_fee': 0}
# 	cart['cart_value'] = 10000
# 	content = get_delivery_fee_content(cart)
# 	assert content == {'delivery_fee': 0}
