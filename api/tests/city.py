from app import app
from app.models.base import db
from app.models.city import City
from app.models.state import State
import unittest
import logging


class city_test(unittest.TestCase):
    def setUp(self):
        # disabling logs
        # logging.disable(logging.CRITICAL)
        self.app = app.test_client()
        # connecting to the database
        db.connect()
        db.create_tables([State], safe=True)
        db.create_tables([City], safe=True)

    def tearDown(self):
        # deleting database
        db.drop_tables([City])
        db.drop_tables([State])

    def test_create(self):
        # creating a state
        new_state = self.app.post('/states', data=dict(name='California'))
        assert new_state.status_code == 200
        # print new_state.status_code
        # creating a city
        new_city = self.app.post('/states/1/cities', data=dict(name='San Francisco'))
        assert new_city.status_code == 200
        # creating the same city in the same state
        new_city = self.app.post('/states/1/cities', data=dict(name='San Francisco'))
        assert new_city.status_code == 409

        # creating a state
        new_state = self.app.post('/states', data=dict(name='Oregon'))
        assert new_state.status_code == 200
        # print new_state.status_code
        # creating the same city in different state
        new_city = self.app.post('/states/2/cities', data=dict(name='San Francisco'))
        assert new_city.status_code == 200


    def test_get(self):
        # creating a state
        new_state = self.app.post('/states', data=dict(name='California'))
        assert new_state.status_code == 200
        # print new_state.status_code
        # creating a city
        new_city = self.app.post('/states/1/cities', data=dict(name='San Francisco'))
        # print new_city.data
        assert new_city.status_code == 200
        # getting city
        get_city = self.app.get('/states/1/cities')
        # print get_city.data
        assert get_city.status_code == 200

    def test_delete(self):
        # creating a state
        new_state = self.app.post('/states', data=dict(name='California'))
        assert new_state.status_code == 200
        # print new_state.status_code
        # creating a city
        new_city = self.app.post('/states/1/cities', data=dict(name='San Francisco'))
        assert new_city.status_code == 200
        # deleting the city
        city_delete = self.app.delete('/states/1/cities/1')
        assert city_delete.status_code == 200
