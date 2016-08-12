from base import *
from peewee import *
from user import User
from review import Review

'''
 ReviewUser:
    - user: foreign key to User
    - review: foreign key to Review
'''
class ReviewUser(BaseModel):
    user = ForeignKeyField(User)
    review = ForeignKeyField(Review)


class Meta():
    database = db
