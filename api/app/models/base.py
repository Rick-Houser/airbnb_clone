import peewee
from datetime import datetime
from config import *


db = peewee.MySQLDatabase( DATABASE['database'],
                            host=DATABASE['host'],
                            port=DATABASE['port'],
                            user=DATABASE['user'],
                            charset= DATABASE['charset'],
                            passwd=DATABASE['password'])

class BaseModel(peewee.Model):
    id = peewee.PrimaryKeyField(unique=True)
    updated_at = peewee.DateTimeField(default=datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    create_at = peewee.DateTimeField(default=datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

    def save (self, *args,  **kwargs):
        self.updated_at = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        peewee.Model.save(self)


    class Meta():
        database = db
        ordered_by =("id", )
