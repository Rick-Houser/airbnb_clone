from base import *
from peewee import *
from user import User
from review import Review


class ReviewUser(Model):
    user = ForeignKeyField(User)
    review = ForeignKeyField(Review)


class Meta():
    database = db
