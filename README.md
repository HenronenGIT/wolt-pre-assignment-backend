#  HTTP Backend API - Pre-assignment for backend Internship position at Wolt

## Tech

<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"></img>
<img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"></img>


## Description

Backend API with single endpoint made with FastAPI. 

##  How to use
1. `pip install -r requirements.txt`
2. `uvicorn main:app`
3. Testing can be done with the command `pytest`

API is running in port 8000

### The Task

**TLDR;**

Implement an HTTP API (single endpoint) which calculates the delivery fee based on the information in the request payload (JSON) and includes the calculated delivery fee in the response payload (JSON).

<details>
<summary>Click to see whole description of the task</summary>
Your task is to build an HTTP API which could be used for calculating the delivery fee.

Please implement your solution in either **Python, Kotlin or Scala**. Feel free to use libraries / frameworks.

**Note that your technology choice here defines the scope the possible technical interview and your focus area if starting to work at Wolt 😊**


### Specification
Implement an HTTP API (single endpoint) which calculates the delivery fee based on the information in the request payload (JSON) and includes the calculated delivery fee in the response payload (JSON).

#### Request
Example: 
```json
{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}
```

##### Field details

| Field             | Type  | Description                                                           | Example value                             |
|:---               |:---   |:---                                                                   |:---                                       |
|cart_value         |Integer|Value of the shopping cart __in cents__.                               |__790__ (790 cents = 7.90€)                |
|delivery_distance  |Integer|The distance between the store and customer’s location __in meters__.  |__2235__ (2235 meters = 2.235 km)          |
|number_of_items    |Integer|The __number of items__ in the customer's shopping cart.               |__4__ (customer has 4 items in the cart)   |
|time               |String |Order time in [ISO format](https://en.wikipedia.org/wiki/ISO_8601).    |__2021-01-16T13:00:00Z__                   |

#### Response
Example:
```json
{"delivery_fee": 710}
```

##### Field details

| Field         | Type  | Description                           | Example value             |
|:---           |:---   |:---                                   |:---                       |
|delivery_fee   |Integer|Calculated delivery fee __in cents__.  |__710__ (710 cents = 7.10€)|

</details>


## Endpoint

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
