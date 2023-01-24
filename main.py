from models.cart import Cart_Model
from fastapi import FastAPI
from utils.helpers import *

app = FastAPI()

@app.get("/delivery_fee")
async def create_item(cart: Cart_Model) -> dict:
	FREE_DELIVERY_THRESHOLD = 10000
	SMALL_SURCHARGE_THRESHOLD = 1000
	MAX_DELIVERY_FEE = 15000
	ITEM_COUNT_THRESHOLD = 5
	RUSH_HOUR_MULTIPLIER = 1.2
	
	fee = 0
	if (cart.cart_value >= FREE_DELIVERY_THRESHOLD):
		return {"delivery_fee": 0}
	fee += calculate_distance_fee(cart.delivery_distance)
	if (cart.cart_value < SMALL_SURCHARGE_THRESHOLD):
		fee += calculate_small_surcharge(cart.cart_value)
	if (cart.number_of_items >= ITEM_COUNT_THRESHOLD):
		fee += calculate_item_fee(cart.number_of_items)
	if (rush_hour(cart.time)):
		fee *= RUSH_HOUR_MULTIPLIER
	fee = min(fee, MAX_DELIVERY_FEE)
	return {"delivery_fee": fee}
