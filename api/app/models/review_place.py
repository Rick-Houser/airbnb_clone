from base import db
from peewee import *
from place import Place
from review import Review


class ReviewPlace(peewee.Model):
    place = ForeignKeyField(Place)
    review = ForeinKeyField(Review)


class Meta():
    database = db
