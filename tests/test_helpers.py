from utils.helpers import *

def test_delivery_distance():
	PER_METER_FEE = 100
	BASE_FEE = 200
	base_fee_distances = [
		400,
		1,
		0,
		999,
	]
	for distance in base_fee_distances:
		fee = calculate_distance_fee(distance)
		assert fee == BASE_FEE

	fee = calculate_distance_fee(1499)
	assert fee == BASE_FEE + PER_METER_FEE

	fee = calculate_distance_fee(1500)
	assert fee == BASE_FEE + PER_METER_FEE

	fee = calculate_distance_fee(1501)
	assert fee == BASE_FEE + PER_METER_FEE * 2

	fee = calculate_distance_fee(1600)
	assert fee == 400

def test_small_surcharge():
	test_values = [
		1,
		500,
		999
		]

	for value in test_values:
		base = 1000
		fee = calculate_small_surcharge(value)
		assert fee == base - value

def test_item_count_fee():
	fee = calculate_item_count_fee(1)
	assert fee == 0
	fee = calculate_item_count_fee(5)
	assert fee == 50
	fee = calculate_item_count_fee(10)
	assert fee == 300
	fee = calculate_item_count_fee(13)
	assert fee == 570

def test_rush_hour():
	RUSH_HOUR_MULTIPLIER = 1.2
	rush_hours = [
		("2013-3-22T15:00:00Z", 500),
		("2004-2-13T16:00:00Z", 600),
		("2023-1-20T19:00:00Z", 100)
		]

	for time, test_fee in rush_hours:
		assert calculate_rush_hour_fee(time, test_fee) == test_fee * RUSH_HOUR_MULTIPLIER

def test_not_rush_hour():
	not_rush_hours = [
		("2023-1-20T14:00:00Z", 500),
		("2023-1-20T20:00:00Z", 600),
		("2004-2-16T19:00:00Z", 100),
		("2020-1-20T15:00:00Z", 100),
		]

	for time, test_fee in not_rush_hours:
		assert calculate_rush_hour_fee(time, test_fee) == test_fee
