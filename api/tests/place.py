from app import app
import unittest
import logging
from app.models.base import db
from app.models.place import Place
from app.models.city import City
from app.models.state import State
from app.models.user import User
from flask import jsonify


class place_test(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        logging.disable(logging.CRITICAL)
        # connectting to database
        db.connect()
        db.create_tables([User], safe=True)
        db.create_tables([State], safe=True)
        db.create_tables([City], safe=True)
        db.create_tables([Place], safe=True)

    def tearDown(self):
        # deleting database
        db.drop_tables([Place])
        db.drop_tables([City])
        db.drop_tables([User])
        db.drop_tables([State])

    # def test_create(self):
    #     # creating a new state depency of city
    #     new_state = self.app.post('/states', data=dict(name='California'))
    #     assert new_state.status_code == 200
    #     # creating a new city
    #     new_city = self.app.post('/states/1/cities', data=dict(name='San Francisco'))
    #     assert new_city.status_code == 200
    #     # creating a new user dependency for place
    #     new_user = self.app.post('/users', data=dict(first_name='Jon',
    #                                                  last_name='Snow',
    #                                                  email='jon@snow',
    #                                                  password='toto1234'))
    #     assert new_user.status_code == 200
    #     # creating a place
    #     new_place = self.app.post('/places', data=dict(
    #                                          owner=1,
    #                                          city=1,
    #                                          name="Steven",
    #                                          description="house",
    #                                          number_rooms=3,
    #                                          number_bathrooms=2,
    #                                          max_guest=3,
    #                                          price_by_night=100,
    #                                          latitude=37.774929,
    #                                          longitude=-122.419416))
    #     assert new_place.status_code == 200
    #     # Getting place
    #     get_place = self.app.get('/places')
    #     # print get_place.data
    #     assert get_place.status_code == 200
    #
    # def test_get(self):
    #     # creating a new state depency of city
    #     new_state = self.app.post('/states', data=dict(name='California'))
    #     assert new_state.status_code == 200
    #     # creating a new city
    #     new_city = self.app.post('/states/1/cities', data=dict(name='San Francisco'))
    #     assert new_city.status_code == 200
    #     # creating a new user dependency for place
    #     new_user = self.app.post('/users', data=dict(first_name='Jon',
    #                                                  last_name='Snow',
    #                                                  email='jon@snow',
    #                                                  password='toto1234'))
    #     assert new_user.status_code == 200
    #     # creating a place
    #     new_place = self.app.post('/places', data=dict(
    #                                          owner=1,
    #                                          city=1,
    #                                          name="Steven",
    #                                          description="house",
    #                                          number_rooms=3,
    #                                          number_bathrooms=2,
    #                                          max_guest=3,
    #                                          price_by_night=100,
    #                                          latitude=37.774929,
    #                                          longitude=-122.419416))
    #     assert new_place.status_code == 200
    #     # creating a place 2
    #     new_place2 = self.app.post('/places', data=dict(
    #                                          owner=1,
    #                                          city=1,
    #                                          name="Steven apartment",
    #                                          description="apartment",
    #                                          number_rooms=1,
    #                                          number_bathrooms=1,
    #                                          max_guest=2,
    #                                          price_by_night=100,
    #                                          latitude=37.774929,
    #                                          longitude=-122.419416))
    #     assert new_place2.status_code == 200
    #     # Getting place 2
    #     get_place = self.app.get('/places/2')
    #     assert get_place.status_code == 200
    #     # Getting place 1
    #     get_place = self.app.get('/places/1')
    #     assert get_place.status_code == 200
    #     # Getting place that does not exist
    #     get_place = self.app.get('/places/3')
    #     assert get_place.status_code == 404
    #
    #     # Trying to update place
    #     new_update = self.app.put('/places/2', data=dict(city=2))
    #     # print new_update.status_code
    #     assert new_update.status_code == 409
    #     new_update = self.app.put('/places/2', data=dict(owner=2))
    #     # print new_update.data
    #     assert new_update.status_code == 409
    #     new_update = self.app.put('/places/2', data=dict(price_by_night=50))
    #     # print new_update.data
    #     assert new_update.status_code == 200
    #     new_update = self.app.put('/places/2', data=dict(name='updated_data'))
    #     assert new_update.status_code == 200
    #     new_update = self.app.put('/places/2', data=dict(description='update'))
    #     assert new_update.status_code == 200
    #     new_update = self.app.put('/places/2', data=dict(max_guest=1))
    #     assert new_update.status_code == 200
    #     new_update = self.app.put('/places/2', data=dict(number_bathrooms=2))
    #     assert new_update.status_code == 200
    #     # deleting place
    #     new_delete = self.app.delete('/places/1')
    #     # print new_delete.status_code
    #     assert new_delete.status_code == 200
    #     # deleting place that does not exist
    #     get_place = self.app.delete('/places/3')
    #     assert get_place.status_code == 404
    #
    # def test_update(self):
    #     # creating a new state depency of city
    #     new_state = self.app.post('/states', data=dict(name='California'))
    #     assert new_state.status_code == 200
    #     # creating a new city
    #     new_city = self.app.post('/states/1/cities', data=dict(name='San Francisco'))
    #     assert new_city.status_code == 200
    #     # creating a new user dependency for place
    #     new_user = self.app.post('/users', data=dict(first_name='Jon',
    #                                                  last_name='Snow',
    #                                                  email='jon@snow',
    #                                                  password='toto1234'))
    #     assert new_user.status_code == 200
    #     new_place = self.app.post('/places', data=dict(
    #                                          owner=1,
    #                                          city=1,
    #                                          name="Steven apartment",
    #                                          description="apartment",
    #                                          number_rooms=1,
    #                                          number_bathrooms=1,
    #                                          max_guest=2,
    #                                          price_by_night=100,
    #                                          latitude=37.774929,
    #                                          longitude=-122.419416))
    #     assert new_place.status_code == 200
    #     get_place = self.app.get('/states/1/cities/1/places')
    #     assert get_place.status_code == 200
    #     new_place = self.app.post('/places', data=dict(
    #                                          owner=1,
    #                                          city=1,
    #                                          name="Steven",
    #                                          description="House",
    #                                          number_rooms=5,
    #                                          number_bathrooms=3,
    #                                          max_guest=8,
    #                                          price_by_night=100,
    #                                          latitude=37.774929,
    #                                          longitude=-122.419416))
    #     assert new_place.status_code == 200
    #     get_place = self.app.get('/states/1/cities/1/places')
    #     assert get_place.status_code == 200
    #
    #     create_place = self.app.post('/states/1/cities/1/places',
    #                                  data=dict(owner=1,
    #                                            name="Brittney",
    #                                            description="Clastle",
    #                                            number_rooms=50,
    #                                            number_bathrooms=10,
    #                                            max_guest=200,
    #                                            price_by_night=1000,
    #                                            latitude=37.774929,
    #                                            longitude=-122.419416))
    #     assert create_place.status_code == 200

    def test_place_state(self):
        # creating a new state depency of city
        new_state = self.app.post('/states', data=dict(name='California'))
        assert new_state.status_code == 200
        # creating a new city
        new_city = self.app.post('/states/1/cities', data=dict(name='San Francisco'))
        assert new_city.status_code == 200
        # creating a new user dependency for place
        new_user = self.app.post('/users', data=dict(first_name='Jon',
                                                     last_name='Snow',
                                                     email='jon@snow',
                                                     password='toto1234'))
        assert new_user.status_code == 200
        # creating a place
        new_place = self.app.post('/places', data=dict(
                                             owner=1,
                                             city=1,
                                             name="Steven",
                                             description="house",
                                             number_rooms=3,
                                             number_bathrooms=2,
                                             max_guest=3,
                                             price_by_night=100,
                                             latitude=37.774929,
                                             longitude=-122.419416))
        assert new_place.status_code == 200

        # getting a place for a state that exist
        get_place_state = self.app.get('/states/1/places')
        assert get_place_state.status_code == 200

        # getting a place for a state that does not exist
        get_place_state = self.app.get('/states/3/places')
        assert get_place_state.status_code == 404
