from peewee import *
from amenity import *
from place import *
from base import *


class PlaceAmenities(BaseModel):
    place = ForeignKeyField(Place)
    amenity = ForeignKeyField(Amenity)

    # class Meta():
    #     database = db
