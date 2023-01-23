import requests
import json

FEE_URL = "http://localhost:8000/delivery_fee"

def get_delivery_fee_status(cart: dict):
	response = requests.get(FEE_URL, json = cart)
	return response.status_code

def get_delivery_fee_content(cart: dict):
	response = requests.get(FEE_URL, json = cart)
	return json.loads(response.content)