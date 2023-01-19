import json
from fastapi import FastAPI
from pydantic import BaseModel
from utils.helpers import *

app = FastAPI()

# {"cart_value": 790, "delivery_distance": 2235,
# "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}


class Cart_Model(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: str

# Landing page


@app.get("/")
async def root():
	temp = {}
	temp["root"] = "root"
	return temp

# Delivery fee


@app.get("/delivery_fee")
async def create_item(cart: Cart_Model):
	FREE_DELIVERY_THRESHOLD = 10000
	MAX_DELIVERY_FEE = 15000

	cart = cart.dict()
	fee = 0
	result = {}
	result["delivery_fee"] = 0

	if cart['cart_value'] >= FREE_DELIVERY_THRESHOLD:
		result
	# if cart["cart_value"] < 1000:
		# fee += calculate_small_surcharge(cart["cart_value"])
	# fee += calculate_distance_fee(cart["delivery_distance"])
	if cart["number_of_items"] >= 5:
		fee += calculate_item_fee(cart["number_of_items"])

	if fee > MAX_DELIVERY_FEE:
		fee = MAX_DELIVERY_FEE
	result["delivery_fee"] = fee
	return result
