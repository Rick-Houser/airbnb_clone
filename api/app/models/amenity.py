from peewee import *
from base import *

class Amenity(BaseModel):
    name = CharField(128, null = False)
