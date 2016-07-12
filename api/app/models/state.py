from peewee import *
from base import *


class State(BaseModel):
    name = CharField(128, null = False, unique = True)
