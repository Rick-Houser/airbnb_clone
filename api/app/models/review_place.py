from base import *
from peewee import *
from place import Place
from review import Review

'''
 ReviewPlace:
    - place: foreign key to Place
    - review: foreign key to Review
'''
class ReviewPlace(BaseModel):
    place = ForeignKeyField(Place)
    review = ForeignKeyField(Review)


class Meta:
    database = db
