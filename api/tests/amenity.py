from app import app
from app.models.base import db
from app.models.amenity import Amenity
from app.models.place_amenity import PlaceAmenities
from app.models.place import Place
from app.models.city import City
from app.models.state import State
from app.models.user import User
import unittest
import logging


class AmenitiesTest(unittest.TestCase):
    # Disable logging calls with levels less severe than or equal to CRITICAL.
    # connect to database and create table for testing.
    def setUp(self):
        logging.disable(logging.CRITICAL)
        self.app = app.test_client()
        db.connect()
        db.create_tables([User], safe=True)
        db.create_tables([State], safe=True)
        db.create_tables([City], safe=True)
        db.create_tables([Place], safe=True)
        db.create_tables([Amenity], safe=True)
        db.create_tables([PlaceAmenities], safe=True)

    # Drop test table
    def tearDown(self):
        db.drop_tables([PlaceAmenities], safe=True)
        db.drop_tables([Amenity], safe=True)
        db.drop_tables([Place], safe=True)
        db.drop_tables([City], safe=True)
        db.drop_tables([State], safe=True)
        db.drop_tables([User], safe=True)

    # Create new amenity
    def test_post(self):
        new_amenity = self.app.post('/amenities',
                                    data=dict(name='amenity1'))
        assert new_amenity.status_code == 200

    def test_get(self):
        # Creating a new amenity
        new_amenity = self.app.post('/amenities',
                                    data=dict(name='amenity1'))
        assert new_amenity.status_code == 200

        get_amenity = self.app.get('/amenities/1',
                                   data=dict(name='amenity1'))
        assert get_amenity.status_code == 200

        # Get newly created amenity. 404 (Not Found) if amenity doesn't exist.
        get_invalid_amenity = self.app.get('/amenities/9',
                                           data=dict(name='amenity1'))
        assert get_invalid_amenity.status_code == 404

    # Delete newly created amenity.404 (Not Found) if amenity doesn't exist
    def test_delete(self):
        new_amenity = self.app.post('/amenities',
                                    data=dict(name='amenity1'))
        assert new_amenity.status_code == 200

        get_amenity = self.app.delete('/amenities/1',
                                      data=dict(name='amenity1'))
        assert get_amenity.status_code == 200

        get_amenity = self.app.delete('/amenities/9',
                                      data=dict(name='amenity1'))
        assert get_amenity.status_code == 404

    def test_Place_amenities(self):
        new_state = State(name='California')
        new_state.save()
        new_city = City(name='San Francisco', state=1)
        new_city.save()
        # Creating a new users
        user1 = User(first_name='Jon',
                     last_name='Snow',
                     email='jon@snow',
                     password='toto1234')
        user1.save()
        # Creating Place
        new_place = Place(owner=1,
                          city=1,
                          name="Steven",
                          description="house",
                          number_rooms=3,
                          number_bathrooms=2,
                          max_guest=3,
                          price_by_night=100,
                          latitude=37.774929,
                          longitude=-122.419416)
        new_place.save()
        # Creating an amenity
        new_amenity = Amenity(name="amenity1")
        new_amenity.save()

        # Creating a place amenity

        new_place_amenity = PlaceAmenities(place=1, amenity=1)
        new_place_amenity.save()

        # Creating amenity test for different user
        new_state = State(name='Oregon')
        new_state.save()
        new_city = City(name='San Francisco', state=1)
        new_city.save()

        # Creating a new users 2
        user1 = User(first_name='Jon',
                     last_name='Snow',
                     email='jon+1c@snow',
                     password='toto1234')
        user1.save()

        # Creating Place 2
        new_place = Place(owner=2,
                          city=2,
                          name="Steven",
                          description="house",
                          number_rooms=3,
                          number_bathrooms=2,
                          max_guest=3,
                          price_by_night=100,
                          latitude=37.774929,
                          longitude=-122.419416)
        new_place.save()
        # Creating an amenity 2
        new_amenity = Amenity(name="amenity2")
        new_amenity.save()

        # Creating a place amenity 1
        new_place_amenity = PlaceAmenities(place=1, amenity=1)
        new_place_amenity.save()

        # Creating a place amenity 2
        new_place_amenity = PlaceAmenities(place=2, amenity=2)
        new_place_amenity.save()

        # testing amenities for a different place
        get_place_amenity = self.app.get('/places/1/amenities')
        assert get_place_amenity.status_code == 200

        # testing amenities for a different place
        get_place_amenity = self.app.get('/places/2/amenities')
        assert get_place_amenity.status_code == 200

        # testing amenities for a different place that does not exist
        get_place_amenity = self.app.get('/places/3/amenities')
        assert get_place_amenity.status_code == 404
