from peewee import *
from base import *
from state import *
from flask import jsonify


class City(BaseModel):
    name = CharField(128, null = False)
    state = ForeignKeyField(State, related_name= 'cities', on_delete = "CASCADE")

    def to_hash(self):
        return jsonify({'id':self.id,
                'create_at':self.create_at,
                'updated_at':self.updated_at,
                'name':self.name,
                'state_id':self.state
                })
