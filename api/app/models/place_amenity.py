from peewee import *
from amenity import *
from place import *


class PlaceAmenities(Model):
    place = ForeignKeyField(Place)
    amenity = ForeignKeyField(Amenity)
