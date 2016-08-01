from base import *
from place import *
from user import *


class PlaceBook(BaseModel):
    place = ForeignKeyField(Place)
    user = ForeignKeyField(User, related_name="placesbooked")
    is_validated = BooleanField(default=False)
    date_start = DateTimeField(null=False)
    number_nights = IntegerField(default=1)

    def to_dict(self):
        return {'id': self.id,
                'created_at': str(self.created_at.strftime('%d/%m/%Y %H:%M:%S')),
                'updated_at': str(self.updated_at.strftime('%d/%m/%Y %H:%M:%S')),
                'place_id': self.place.id,
                'user_id': self.user.id,
                'is_validated': self.is_validated,
                'date_start': self.date_start,
                'number_nights': self.number_nights
                }
