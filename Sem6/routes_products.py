from models import Product, InputProduct
from fastapi import APIRouter
from db import db, products

router = APIRouter()

@router.get("/products/", response_model=list[Product])
async def read_products():
    query = products.select()
    return await db.fetch_all(query)

@router.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await db.fetch_one(query)

@router.post("/products/add/", response_model=Product)
async def create_product(product: InputProduct):
    query = products.insert().values(
            name=product.name,
            description=product.description,
            price=product.price
            )
    last_record_id = await db.execute(query)
    return {**product.model_dump(), "id": last_record_id}

@router.put("/products/update/{product_id}", response_model=Product)
async def update_product(product_id: int, new_product: InputProduct):
    query = products.update().where(products.c.id == product_id).values(**new_product.model_dump())
    await db.execute(query)
    return {**new_product.model_dump(), "id": product_id}

@router.delete("/products/del/{product_id}")
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await db.execute(query)
    return {'message': f'Product with ID {product_id} was deleted'}