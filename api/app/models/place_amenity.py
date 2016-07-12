from peewee import *
from amenity import *
from place import *

from base import db

class PlaceAmenities(Model):
    place = ForeignKeyField(Place)
    amenity = ForeignKeyField(Amenity)

    class Meta():
        database = db
