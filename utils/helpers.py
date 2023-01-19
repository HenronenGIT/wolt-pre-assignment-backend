# import constant

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
	base_fee = 200
	threshold = 500 #! better name
	per_meter_fee = 100
	distance -= 1000

	if distance % threshold == 0:
		return base_fee + (distance // threshold * per_meter_fee)
	elif distance / threshold < 0:
		return int(base_fee)
	elif distance / threshold < 1:
		return int(base_fee + per_meter_fee)
	else:
		multiplier = distance / threshold
		if multiplier > 1:
			multiplier += 1
		print(multiplier)
		if multiplier > 1:
			base_fee += 100
		return int(base_fee + multiplier * per_meter_fee)

def calculate_item_fee(item_count: int) -> int:
	BULK_FEE_THRESHOLD = 12
	BULK_FEE = 120
	EXTRA_FEE_THRESHOLD = 4
	FEE_PER_ITEM = 50
	
	fee = 0
	if item_count > BULK_FEE_THRESHOLD:
		fee += BULK_FEE
	return fee + ((item_count - EXTRA_FEE_THRESHOLD) * FEE_PER_ITEM)
