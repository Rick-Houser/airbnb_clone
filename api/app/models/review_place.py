from base import *
from peewee import *
from place import Place
from review import Review


class ReviewPlace(Model):
    place = ForeignKeyField(Place)
    review = ForeignKeyField(Review)


class Meta():
    database = db
