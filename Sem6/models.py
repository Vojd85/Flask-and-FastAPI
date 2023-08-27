from pydantic import BaseModel, Field

class InputUser(BaseModel):
    name: str = Field(..., title="Name", min_length=3, max_length=16)
    surname: str = Field(title="Surname", min_length=4, max_length=16)
    email: str = Field(..., title="E-mail", min_length=5, max_length=32)
    password: str = Field(..., title="Password", min_length=6, max_length=16)


class User(InputUser):
    id: int


class InputProduct(BaseModel):
    name : str = Field(..., title="Name", min_length=3, max_length=32)
    description : str = Field(title="Description", max_length=512)
    price: float = Field(..., title="Price", gt=0)


class Product(InputProduct):
    id : int
    

class InputOrder(BaseModel):
    user: int
    product: int
    date: str = Field(...,title="Order date",  max_length=16)
    status: str = Field(title="Status",  max_length=16)


class Order(BaseModel):
    id: int
    user: User
    product: Product
    date_order: str = Field(...,title="Order date",  max_length=16)
    status: str = Field(title="Status",  max_length=16)



