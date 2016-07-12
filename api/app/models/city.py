from peewee import *
from base import *
from state import *

class City(BaseModel):
    name = CharField(128, null = False)
    state = ForeignKeyField(State, related_name= 'cities', on_delete = "CASCADE")
