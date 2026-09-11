from bson import ObjectId
from fastapi import Response

from models.productModel import Product
from dbConnect import products_collection


def serialize_product(product: dict) -> dict:
    product["id"] = str(product.pop("_id"))
    return product

async def create_product_controller(product: Product, response: Response):
    result = await products_collection.insert_one(product.model_dump(exclude={"id"}))
    created = await products_collection.find_one({"_id": result.inserted_id})
    response.status_code = 201
    return {"isSuccess": True, "message": "Product created successfully", "data": serialize_product(created)}


async def get_products_controller():
    products = [serialize_product(product) async for product in products_collection.find()]
    return {"isSuccess": True, "data": products}


async def get_product_by_id(product_id: str, response: Response):
    if not ObjectId.is_valid(product_id):
        response.status_code = 404
        return {"isSuccess": False, "message": "Product not found"}
    product = await products_collection.find_one({"_id": ObjectId(product_id)})
    if product is None:
        response.status_code = 404
        return {"isSuccess": False, "message": "Product not found"}
    return {"isSuccess": True, "data": serialize_product(product)}


async def update_product_controller(product_id: str, product: Product, response: Response):
    if not ObjectId.is_valid(product_id):
        response.status_code = 404
        return {"isSuccess": False, "message": "Product not found"}
    result = await products_collection.replace_one(
        {"_id": ObjectId(product_id)}, product.model_dump(exclude={"id"})
    )
    if result.matched_count == 0:
        response.status_code = 404
        return {"isSuccess": False, "message": "Product not found"}
    product.id = product_id
    return {"isSuccess": True, "message": "Product updated successfully", "data": product}


async def delete_product_controller(product_id: str, response: Response):
    if not ObjectId.is_valid(product_id):
        response.status_code = 404
        return {"isSuccess": False, "message": "Product not found"}
    result = await products_collection.delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count == 0:
        response.status_code = 404
        return {"isSuccess": False, "message": "Product not found"}
    return {"isSuccess": True, "message": "Product deleted successfully"}