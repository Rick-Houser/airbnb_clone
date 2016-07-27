from base import *
from peewee import *
import md5
from datetime import datetime


class User(BaseModel):
    # unique so that there is not a copy in the database of email
    email = CharField(128, null=False, unique=True)
    password = CharField(128, null=False)
    first_name = CharField(128, null=False)
    last_name = CharField(128, null=False)
    is_admin = BooleanField(default=False)

    def set_password(self, clear_password):
        self.password = md5.new(clear_password).hexdigest()

    def to_hash(self):
        return {'id': self.id,
                'created_at': str(self.created_at.strftime('%d/%m/%Y %H:%M:%S')),
                'updated_at': str(self.created_at.strftime('%d/%m/%Y %H:%M:%S')),
                'email': self.email,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'is_admin': self.is_admin
                }
