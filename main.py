from models.cart import Cart_Model
from fastapi import FastAPI
# from pydantic import BaseModel
from utils.helpers import *
from datetime import datetime


app = FastAPI()

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
	ITEM_COUNT_THRESHOLD = 5
	RUSH_HOUR_MULTIPLIER = 1.2

	cart = cart.dict()
	fee = 0
	result = {}
	result["delivery_fee"] = 0
	if (cart['cart_value'] >= FREE_DELIVERY_THRESHOLD):
		return result
	fee += calculate_distance_fee(cart["delivery_distance"])
	if (cart["cart_value"] < 1000):
		fee += calculate_small_surcharge(cart["cart_value"])
	if (cart["number_of_items"] >= ITEM_COUNT_THRESHOLD):
		fee += calculate_item_fee(cart["number_of_items"])
	if (rush_hour(cart['time'])):
		fee *= RUSH_HOUR_MULTIPLIER
	if (fee > MAX_DELIVERY_FEE):
		fee = MAX_DELIVERY_FEE
	result["delivery_fee"] = fee
	return result
