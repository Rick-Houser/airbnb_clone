from base import db
from peewee import *


class ReviewPlace(peewee.Model):
    place = ForeignKeyField(Place)
    review = ForeinKeyField(Review)


class Meta():
    database = db
