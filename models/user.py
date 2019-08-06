from models.base_model import BaseModel
import peewee as pw


class User(BaseModel):
    name = pw.CharField(unique=False) 
    email = pw.CharField(unique=True)
    password = pw.CharField(unique= False, default= "password")
    gender = pw.CharField(unique= False, default= "gender")
    length = pw.CharField(unique= False, default = "length")
    DOB = pw.TextField(unique=False, default= "01/01/2000")
    activity = pw.CharField(unique=False, default="moderate")
    weight = pw.CharField(unique=False, default=0)
   



    def is_authenticated(self):
        return True

    def is_active(self):
        return True


