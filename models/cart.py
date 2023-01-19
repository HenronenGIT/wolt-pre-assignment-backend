from pydantic import BaseModel

class Cart_Model(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: str
