# Wolt Summer 2023 Pre-assignment - Backend

## Description

HTTP backend API with a single endpoint, done with Python FastAPI.

##  How to use
1. `pip install -r requirements.txt`
2. `uvicorn main:app`
3. Testing can be done with the command `pytest`

API is running in port 8000

## Endpoints

### `GET /delivery_fee`

Payload:
```json
	{
		"cart_value": int,
		"delivery_distance": int,
		"number_of_items": int,
		"time": str // format "2021-10-12T13:00:00Z"
	}
```
Respond:
```json
	{"delivery_fee": int}
```
