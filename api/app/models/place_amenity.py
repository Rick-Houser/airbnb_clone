from peewee import *
from amenity import *
from place import *
from base import *

'''
 PlaceAmenities:
    - name: foreign key to Place
    - amenity: foreign key to Amenity
'''
class PlaceAmenities(BaseModel):
    place = ForeignKeyField(Place)
    amenity = ForeignKeyField(Amenity)

    # class Meta():
    #     database = db
