from fastapi import FastAPI
from routers.productRouter import productRouter

app = FastAPI()

app.include_router(productRouter)