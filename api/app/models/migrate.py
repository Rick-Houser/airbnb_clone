from base import db
from user import User
from state import State
from city import City
from place import Place
from place_book import PlaceBook
from amenity import Amenity
from place_amenity import PlaceAmenities

db.connect()
db.create_tables([User,
                  State,
                  City,
                  Place,
                  PlaceBook,
                  Amenity,
                  PlaceAmenities], safe=True)
test = User(email='foo', password='foo', first_name='foo', last_name='foo')
test.save()
