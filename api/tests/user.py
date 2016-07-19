from app import app
import unittest
import logging
from app.models.base import db
from app.models.user import User


class userTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        logging.disable(logging.CRITICAL)
        # connecting to database
        db.connect()
        # creating a database
        db.create_tables([User])

    # def tearDown(self):
        # deleting user
        # User.delete().execute()

    def test_create(self):
        # testing the post request for user with all parameters
        self.app.post('/users', data=dict(first_name='Jon',
                                          last_name='Snow',
                                          email='jon@snow',
                                          password='toto1234'))
        # testing the post request for user without name parameter
        self.app.post('/users', data=dict(first_name=' ',
                                          last_name='Snow',
                                          email='jon+1@snow',
                                          password='toto1234'))
        # testing the post request for user without email parameter
        self.app.post('/users', data=dict(first_name='Jon',
                                          last_name='Snow',
                                          email='jon+2@snow',
                                          password='toto1234'))


        # check user id return should be 1
        self.assertEqual(User.get().id, 1)

        # check can user have the same email

    # def test_list(self):
    #    self.app.get('/users')
