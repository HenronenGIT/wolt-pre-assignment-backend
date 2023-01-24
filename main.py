from fastapi import FastAPI
from routers import delivery_fee

app = FastAPI()
app.include_router(delivery_fee.router)
