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
