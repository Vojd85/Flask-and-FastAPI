from models import Order, InputOrder, User, Product
from fastapi import APIRouter
from db import *

router = APIRouter()

@router.get("/orders/", response_model=list[Order])
async def read_orders():
    query = sqlalchemy.select(
        orders.c.id,
        users.c.id.label('user_id'), users.c.name, users.c.surname, users.c.email,
        products.c.id.label('product_id'), products.c.name.label('product_name'), products.c.description, products.c.price,
        orders.c.date, orders.c.status
        ).join(users).join(products)
    rows = await db.fetch_all(query)
    return [Order(id=row.id, 
                  user=User(id=row.user_id, name=row.name, surname=row.surname, 
                            email=row.email, password="*******"),
                  product= Product(id=row.product_id, name=row.product_name, 
                                   description=row.description, price=row.price),  
                  date_order=row.date, status=row.status
                  ) for row in rows]

@router.get("/orders/{order_id}", response_model=dict)
async def read_order(order_id: int):
    query = sqlalchemy.select(
        orders.c.id,
        users.c.id.label('user_id'), users.c.name, users.c.surname, users.c.email,
        products.c.id.label('product_id'), products.c.name.label('product_name'), products.c.description, products.c.price,
        orders.c.date, orders.c.status
        ).join(users).join(products).where(orders.c.id == order_id)
    row = await db.fetch_one(query)
    order = Order(id=row.id, 
                  user=User(id=row.user_id, name=row.name, surname=row.surname, 
                            email=row.email, password="*******"),
                  product= Product(id=row.product_id, name=row.product_name, 
                                   description=row.description, price=row.price),  
                  date_order=row.date, status=row.status
                )
    return {**order.model_dump()}

@router.post("/orders/add/", response_model=dict)
async def create_order(order: InputOrder):
    query = orders.insert().values(
            user=order.user,
            product=order.product,
            date=order.date,
            status=order.status
            )
    last_record_id = await db.execute(query)
    return {**order.model_dump(), "id": last_record_id}

@router.put("/orders/update/{order_id}", response_model=dict)
async def update_orders(order_id: int, new_order: InputOrder):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.model_dump())
    await db.execute(query)
    return {**new_order.model_dump(), "id": order_id}

@router.delete("/orders/del/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await db.execute(query)
    return {'message': f'Order with ID {order_id} was deleted'}