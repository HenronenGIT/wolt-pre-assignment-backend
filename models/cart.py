from pydantic import BaseModel, validator, PositiveInt


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
