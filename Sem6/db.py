import databases
import sqlalchemy
from settings import settings

db = databases.Database(settings.DATABASE_URL)
metadata = sqlalchemy.MetaData()

products = sqlalchemy.Table("products", metadata,
            sqlalchemy.Column("id", sqlalchemy.Integer,primary_key=True),
            sqlalchemy.Column("name", sqlalchemy.String(32)),
            sqlalchemy.Column("description", sqlalchemy.String(512)),
            sqlalchemy.Column("price", sqlalchemy.Float),
            )

users = sqlalchemy.Table("users", metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column("name", sqlalchemy.String(16)),        
        sqlalchemy.Column("surname", sqlalchemy.String(16)),
        sqlalchemy.Column("email", sqlalchemy.String(32)),
        sqlalchemy.Column("password", sqlalchemy.String(16)),
        )

orders = sqlalchemy.Table("orders", metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column("user", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id')),
        sqlalchemy.Column("product", sqlalchemy.Integer, sqlalchemy.ForeignKey('products.id')),
        sqlalchemy.Column("date", sqlalchemy.String(10)),
        sqlalchemy.Column("status", sqlalchemy.String(16))  
        )

engine = sqlalchemy.create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False})
metadata.create_all(engine)


