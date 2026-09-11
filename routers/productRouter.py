from fastapi import APIRouter, Response

from controllers.productController import (
    create_product_controller,
    delete_product_controller,
    get_product_by_id,
    get_products_controller,
    update_product_controller,
)
from models.productModel import Product


productRouter = APIRouter(prefix="/products", tags=["products"])


@productRouter.post("/")
async def create_product(product: Product, response: Response):
    return await create_product_controller(product, response)


@productRouter.get("/")
async def get_products():
    return await get_products_controller()


@productRouter.get("/{product_id}")
async def get_product(product_id: str, response: Response):
    return await get_product_by_id(product_id, response)


@productRouter.put("/{product_id}")
async def update_product(product_id: str, product: Product, response: Response):
    return await update_product_controller(product_id, product, response)


@productRouter.delete("/{product_id}")
async def delete_product(product_id: str, response: Response):
    return await delete_product_controller(product_id, response)