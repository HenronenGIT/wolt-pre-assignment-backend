from models.cart import Cart_Model
from fastapi import FastAPI
from utils.helpers import *

app = FastAPI()

@app.get("/delivery_fee")
async def calculate_delivery_fee(cart: Cart_Model) -> dict:
	"""
	Endpoint to calculate delivery fee based on received payload.
	---
	responses:
			200:
				description: Delivery fee returned successfully.
			422:
				description: Invalid values in the received payload.
	"""
	FREE_DELIVERY_THRESHOLD = 10000
	SMALL_SURCHARGE_THRESHOLD = 1000
	MAX_DELIVERY_FEE = 15000
	ITEM_COUNT_THRESHOLD = 5

	fee = 0
	if (cart.cart_value >= FREE_DELIVERY_THRESHOLD):
		return {"delivery_fee": 0}
	fee += calculate_distance_fee(cart.delivery_distance)
	if (cart.cart_value < SMALL_SURCHARGE_THRESHOLD):
		fee += calculate_small_surcharge(cart.cart_value)
	if (cart.number_of_items >= ITEM_COUNT_THRESHOLD):
		fee += calculate_item_count_fee(cart.number_of_items)
	# if (rush_hour(cart.time)):
		# fee *= RUSH_HOUR_MULTIPLIER
	fee = calculate_rush_hour_fee(cart.time, fee)
	
	fee = min(fee, MAX_DELIVERY_FEE)
	return {"delivery_fee": fee}
