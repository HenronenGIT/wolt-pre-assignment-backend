from utils.helpers import *

BASE_FEE = 200
PER_METER_FEE = 100

def test_rush_hour():
	rush_hours = [
		"2023-1-20T15:00:00Z",
		"2023-1-20T16:00:00Z",
		"2023-1-20T19:00:00Z"
		]

	for time in rush_hours:
		assert rush_hour(time) == True

def test_not_rush_hour():
	not_rush_hours = [
		"2023-1-20T14:00:00Z",
		"2023-1-20T20:00:00Z",
		"2023-1-19T19:00:00Z"
		]
	
	for time in not_rush_hours:
		assert rush_hour(time) == False

def test_not_rush_hour():
	not_rush_hours = [
		"2023-1-20T14:00:00Z",
		"2023-1-20T20:00:00Z",
		"2023-1-19T19:00:00Z"
		]
	
	for time in not_rush_hours:
		assert rush_hour(time) == False

def test_delivery_distance():
	cart = {
		"cart_value": 1000,
		"delivery_distance": 1,
		"number_of_items": 1,
		"time": "2021-10-12T13:00:00Z"
	}
	fee = calculate_distance_fee(cart["delivery_distance"])
	assert fee == BASE_FEE

	cart["delivery_distance"] = 1499
	fee = calculate_distance_fee(cart["delivery_distance"])
	assert fee == BASE_FEE + PER_METER_FEE

	cart["delivery_distance"] = 1500
	fee = calculate_distance_fee(cart["delivery_distance"])
	assert fee == BASE_FEE + PER_METER_FEE

	cart["delivery_distance"] = 1501
	fee = calculate_distance_fee(cart["delivery_distance"])
	assert fee == BASE_FEE + PER_METER_FEE * 2

def test_small_surcharge():
	cart = {
		"cart_value": 1000,
		"delivery_distance": 1,
		"number_of_items": 1,
		"time": "2021-10-12T13:00:00Z"
	}
	# calculate_distance_fee()

