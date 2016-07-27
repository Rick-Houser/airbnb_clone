from peewee import *
from base import *
from state import *
from datetime import datetime


class City(BaseModel):
    name = CharField(128, null=False)
    state = ForeignKeyField(State, related_name='cities', on_delete="CASCADE")

    def to_hash(self):
        hash = {}
        hash["id"] = self.id
        hash["created_at"] = self.created_at.strftime('%d/%m/%Y %H:%M:%S')
        hash["updated_at"] = self.updated_at.strftime('%d/%m/%Y %H:%M:%S')
        hash["name"] = self.name
        hash["state_id"] = self.state.id
        return hash
        # return {'id': self.id,
        #         'created_at': self.created_at.strftime('%d/%m/%Y %H:%M:%S'),
        #         'updated_at': self.updated_at.strftime('%d/%m/%Y %H:%M:%S'),
        #         'name': self.name,
        #         'state_id': self.state
        #         }
