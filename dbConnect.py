import os

from motor.motor_asyncio import AsyncIOMotorClient


mongo_url = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(mongo_url)
db = client[os.getenv("MONGODB_DATABASE", "products_db")]
products_collection = db["products"]