from models import User, InputUser
from fastapi import APIRouter
from db import db, users

router = APIRouter()

@router.get("/users/", response_model=list[User])
async def read_users():
    query = users.select()
    return await db.fetch_all(query)

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await db.fetch_one(query)

@router.post("/users/add/", response_model=User)
async def create_user(user: InputUser):
    query = users.insert().values(
            name=user.name,
            surname=user.surname,
            email=user.email,
            password=user.password
            )
    last_record_id = await db.execute(query)
    return {**user.model_dump(), "id": last_record_id}

@router.put("/users/update/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: InputUser):
    query = users.update().where(users.c.id == user_id).values(**new_user.model_dump())
    await db.execute(query)
    return {**new_user.model_dump(), "id": user_id}

@router.delete("/users/del/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await db.execute(query)
    return {'message': f'User with ID {user_id} was deleted'}