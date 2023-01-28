# Wolt Summer 2023 Pre-assignment - Backend

## Description

HTTP backend API with a single endpoint, done with Python FastAPI.


##  How to use
1. `pip install -r requirements.txt`
2. `uvicorn main:app`
3. Testing can be done with the command `pytest`
4. If relative error message appears when running tests, run `pip install .`

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

## Note

`setup.py` was not needed on my local machine, but when repo was cloned to new machine,
there was relative import error message when `pytest` was executed. Getting rid of this run `pip install .`

