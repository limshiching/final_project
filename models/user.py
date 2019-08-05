from models.base_model import BaseModel
import peewee as pw


class User(BaseModel):
    name = pw.CharField(unique=False) 
    email = pw.CharField(unique=True)
    password = pw.CharField(unique= False)
    gender = pw.CharField(unique= False)
    length = pw.CharField(unique= False)
    DOB = pw.DateField(unique=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True


