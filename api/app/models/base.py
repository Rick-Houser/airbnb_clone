# import peewee
# from config import *
# from datetime import datetime
#
# db = peewee.MySQLDatabase(DATABASE['database'],
#                           user=DATABASE['user'],
#                           charset=DATABASE['charset'],
#                           host=DATABASE['host'],
#                           port=DATABASE['port'],
#                           passwd=DATABASE['password'])
#
# class BaseModel(peewee.Model):
#     id = peewee.PrimaryKeyField(unique=True)
#     created_at = peewee.DateTimeField(default=datetime.now(), formats='%d/%m/%Y %H:%M:%S') # peewee docs have datetime.datetime.now in exp; might have to check if format comes out right
#     updated_at = peewee.DateTimeField(default=datetime.now(), formats='%d/%m/%Y %H:%M:%S')
#
#     def save(self, *args, **kwargs):
#         self.updated_at = datetime.now()
#         peewee.Model.save(self)  # not sure if this goes before or after self.updated_at assignment
#
#     class Meta:
#         database = db
#         order_by = ("id", )  # what is the extra space for?

import peewee
from datetime import datetime
from config import *
from datetime import datetime


db = peewee.MySQLDatabase(DATABASE['database'],
                          host=DATABASE['host'],
                          port=DATABASE['port'],
                          user=DATABASE['user'],
                          charset=DATABASE['charset'],
                          passwd=DATABASE['password'])


class BaseModel(peewee.Model):
    id = peewee.PrimaryKeyField(unique=True)
    updated_at = peewee.DateTimeField(default=datetime.now())

    created_at = peewee.DateTimeField(default=datetime.now())

    def save(self, *args,  **kwargs):
        self.updated_at = datetime.now()
        peewee.Model.save(self)

    class Meta():
        database = db
        ordered_by = ("id", )
