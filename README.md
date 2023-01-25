# Wolt Summer 2023 Pre-assignment - Backend

##  How to use

1. From the root of your repo run `uvicorn main:app`
2. Testing can be done with the command `pytest`

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
