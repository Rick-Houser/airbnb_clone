from base import *
from place import *
from user import *


class PlaceBook(BaseModel):
    place = ForeignKeyField(Place)
    user = ForeignKeyField(User, related_name="placesbooked")
    is_validated = BooleanField(default=False)
    date_start = DateTimeField(null=False)
    number_nights = IntegerField(default=1)

    def to_hash(self):
        return {'id': self.id,
                'created_at': self.created_at,
                'updated_at': self.updated_at,
                'place_id': self.place,
                'user_id': self.user,
                'is_validated': self.is_validated,
                'date_start': self.date_start,
                'number_nights': self.number_nights
                }
