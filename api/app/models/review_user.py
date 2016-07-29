from base import db
from peewee import *
from user import User
from review import Review


class ReviewUser(peewee.Model):
    user = ForeignKeyField(User)
    review = ForeignKeyField(Review)


class Meta():
    database = db
