# from models.cart import Cart_Model
from fastapi import FastAPI
from utils.helpers import *
from routers import delivery_fee

app = FastAPI()
app.include_router(delivery_fee.router)
