from base import db
from peewee import *


class ReviewUser(peewee.Model):
    user = ForeignKeyField(User)
    review = ForeignKeyField(Review)


class Meta():
    database = db
