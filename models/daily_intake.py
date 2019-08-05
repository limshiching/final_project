from models.base_model import BaseModel
import peewee as pw
from models.user import User


class DailyIntake(BaseModel):
    item_name = pw.CharField(unique= False)
    date = pw.DateField(unique=False)
    sugar_amount = pw.DecimalField(unique=False)
    calories = pw.DecimalField(unique=False)
    user = pw.ForeignKeyField(User, backref="daily_intake")
