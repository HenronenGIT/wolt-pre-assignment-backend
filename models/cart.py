from pydantic import BaseModel, validator, PositiveInt
from dateutil.parser import parse

class Cart_Model(BaseModel):
	cart_value: PositiveInt
	number_of_items: PositiveInt
	delivery_distance: int
	time: str

	@validator("delivery_distance")
	def check_delivery_distance(cls, value):
		if value < 0:
			raise ValueError("Invalid value in attribute 'delivery_distance'")
		return value

	# @validator("time")
	# def check_time_format(cls, value):
	# 	try:
	# 		parse(value)
	# 	except ValueError:
	# 		raise ValueError("Invalid time format. It should be in the format 'HH:MM:SS'")
	# 	return value
