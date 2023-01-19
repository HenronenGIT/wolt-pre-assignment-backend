import json
from fastapi import FastAPI
from pydantic import BaseModel
# from utils.helpers import calculate_small_surcharge
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


@app.post("/delivery_fee")
async def create_item(cart: Cart_Model):
	cart = cart.dict()
	fee = 0
	# if cart["cart_value"] < 1000:
		# fee += calculate_small_surcharge(cart["cart_value"])
	fee += calculate_distance_fee(cart["delivery_distance"])





	result = {}
	result["delivery_fee"] = fee
	return result
