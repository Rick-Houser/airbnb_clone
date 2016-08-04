from app import app
import unittest
import logging
from app.models.base import db
from app.models.state import State
import simplejson as json


class state_test(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        # disabling logs
        logging.disable(logging.CRITICAL)
        # connecting to the database
        db.connect()
        # creating a table state_test
        db.create_tables([State], safe=True)

    def tearDown(self):
        # deleting database
        db.drop_tables([State], safe=True)

    def test_create(self):
        # creating a test for creating a new state with post
        new_state = self.app.post('/states', data=dict(name='California'))
        assert new_state.status_code == 200

        # creating another state that contains an already existing state
        new_state = self.app.post('/states', data=dict(name='California'))
        assert new_state.status_code == 409

    def test_list(self):
        # creating new states
        new_state = self.app.post('/states', data=dict(name='California'))
        assert new_state.status_code == 200
        new_state = self.app.post('/states', data=dict(name='Alaska'))
        assert new_state.status_code == 200
        new_state = self.app.post('/states', data=dict(name='Oregon'))
        assert new_state.status_code == 200

        # getting a list of all states
        get_state = self.app.get('/states')
        assert get_state.status_code == 200

    def test_get(self):
        # creating new states
        new_state = self.app.post('/states', data=dict(name='California'))
        assert new_state.status_code == 200

        get_state = self.app.get('/states/1')
        assert get_state.status_code == 200

        # checking if the user created is the same gotten by the request
        assert json.loads(get_state.data)['name'] == 'California'
