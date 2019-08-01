from models.base_model import BaseModel
import peewee as pw
from models.user import User


class Product(BaseModel):
    name = pw.CharField(unique= False)
    consumptiondate = pw.DateField(unique=False)
    sugarlevel = pw.DecimalField(unique=False)
    calories = pw.DecimalField(unique=False)
    user = pw.ForeignKeyField(User, backref="products")
