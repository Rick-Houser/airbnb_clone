from base import *
from peewee import *
import md5
from flask import jsonify


class User(BaseModel):

    email = CharField(128, null=False)
    password = CharField(128, null=False)
    first_name = CharField(128, null=False)
    last_name = CharField(128, null=False)
    is_admin = BooleanField(default=False)

    def set_password(self, clear_password):
        self.password = md5.new(clear_password).hexdigest()

    def to_hash(self):
        return jsonify({'id': self.id,
                        'create_at': self.create_at,
                        'updated_at': self.updated_at,
                        'email': self.email,
                        'first_name': self.first_name,
                        'last_name': self.last_name,
                        'is_admin': self.is_admin
                        })
