from .utils import *

FEE_URL = "http://localhost:8000/delivery_fee"

def test_free_delivery():
	cart = {
		"cart_value": 10000,
		"delivery_distance": 1,
		"number_of_items": 1,
		"time": "2021-10-12T13:00:00Z"
	}
	status_code = get_api_status(cart)
	content = get_api_content(cart)
	assert status_code == 200
	assert content == {"delivery_fee": 0}

def test_invalid_payload():
	invalid_carts = [
	{
		"cart_value": -1,
		"delivery_distance": 1,
		"number_of_items": 1,
		"time": "2021-10-12T13:00:00Z"
	},
	{
		"cart_value": 100,
		"delivery_distance": -500,
		"number_of_items": 1,
		"time": "2021-10-12T13:00:00Z"
	},
	{
		"cart_value": 100,
		"delivery_distance": 1000,
		"number_of_items": -42,
		"time": "2021-10-12T13:00:00Z"
	},
	{
		"cart_value": 100,
		"delivery_distance": 1000,
		"number_of_items": -42,
		"time": "2021-10-12T13:00:00Z"
	},
	]
	for cart in invalid_carts:
		status = get_api_status(cart)
		assert status == 422

def test_free_delivery():
	cart = {
		"cart_value": 10000,
		"delivery_distance": 1,
		"number_of_items": 1,
		"time": "2021-10-12T13:00:00Z"
	}
	content = get_api_content(cart)
	assert content == {'delivery_fee': 0}

def test_max_delivery_fee():
	cart = {
		"cart_value": 50000,
		"delivery_distance": 10000,
		"number_of_items": 10,
		"time": "2023-10-12T13:00:00Z"
	}
	content = get_api_content(cart)
	assert content == {'delivery_fee': 0}

# def test_rush_hour_fee():
# 	cart = {
# 		"cart_value": 100,
# 		"delivery_distance": 500,
# 		"number_of_items": 4,
# 		"time": "2020-1-3T16:00:00Z"
# 	}
# 	content = get_api_content(cart)
# 	assert content == {'delivery_fee': 0}

