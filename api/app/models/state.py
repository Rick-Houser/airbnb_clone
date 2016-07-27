from base import *


class State(BaseModel):
    name = peewee.CharField(128, null=False, unique=True)

    def to_hash(self):
        return {'id': self.id,
                'created_at': str(self.created_at.strftime('%d/%m/%Y %H:%M:%S')),
                'updated_at': str(self.created_at.strftime('%d/%m/%Y %H:%M:%S')),
                'name': self.name
                }
