# import constant
from datetime import datetime
import pytz

def calculate_small_surcharge(cart_value: int) -> int:
	"""
	Calculates small surcharge fee for the cart.
	Args:
		cart_value (int): The total price of the cart.

	Returns:
		(int): Small surcharge fee.
	"""
	better_name = 1000  # !better name for this
	return better_name - cart_value


def calculate_distance_fee(distance: int) -> int:
	"""
	Calculates the distance fee for the cart.
	Args:
		distance (int): The original price of the item.

	Returns:
		(int): The distance fee.
	"""
	BASE_FEE = 200
	THRESHOLD = 500 #! better name
	PER_METER_FEE = 100

	if distance <= 1000:
		return BASE_FEE
	distance -= 1000
	multiplier = 1
	multiplier = distance // THRESHOLD
	if distance % 500:
		multiplier += 1
	return int(PER_METER_FEE * multiplier + BASE_FEE)

def calculate_item_fee(item_count: int) -> int:
	BULK_FEE_THRESHOLD = 12
	BULK_FEE = 120
	EXTRA_FEE_THRESHOLD = 4
	FEE_PER_ITEM = 50
	
	fee = 0
	if item_count > BULK_FEE_THRESHOLD:
		fee += BULK_FEE
	return fee + ((item_count - EXTRA_FEE_THRESHOLD) * FEE_PER_ITEM)

def rush_hour(current_time: str) -> bool:
	"""
	Receives current time and checks that is it a rush hour in UTC timezone.
	Args:
		current_time (str)
	Returns:
		(bool): If it is rush hour, returns True (bool
	"""
	RUSH_HOUR_START = "15:00"
	RUSH_HOUR_END = "19:00"
	MULTIPLIER = 1.2
	FRIDAY = 4

	current = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%SZ")
	if current.weekday() != FRIDAY:
		return (False)
	start = datetime.strptime(RUSH_HOUR_START, "%H:%M")
	end = datetime.strptime(RUSH_HOUR_END, "%H:%M")
	if start.time() <= current.time() <= end.time():
		return (True)
	return (False)
	
