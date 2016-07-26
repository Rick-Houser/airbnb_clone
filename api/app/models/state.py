from base import *


class State(BaseModel):
    name = peewee.CharField(128, null=False, unique=True)

    def to_hash(self):
        hash = {}
        hash["id"] = self.id
        hash["created_at"] = self.created_at.strftime('%d/%m/%Y %H:%M:%S')
        hash["updated_at"] = self.updated_at.strftime('%d/%m/%Y %H:%M:%S')
        hash["name"] = self.name
        return hash
