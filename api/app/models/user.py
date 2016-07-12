from base import *
from peewee import *
import md5

class User(BaseModel):

    email= CharField(128,null = False)
    password = CharField(128,null = False)
    first_name = CharField(128,null = False)
    last_name = CharField(128,null = False)
    is_admin = BooleanField(default = False)

    def set_password(self, clear_password):
        self.password = md5.new(clear_password).hexdigest()
