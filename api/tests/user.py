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
        db.create_tables([User], safe=True)

    # def tearDown(self):
        # deleting user
        # User.delete().execute()
        # deleting the table user
        # db.drop_tables([User])

    def test_create(self):
        # testing the post request for user with all parameters
        self.app.post('/users', data=dict(first_name='Jon',
                                          last_name='Snow',
                                          email='jon@snow',
                                          password='toto1234'))
        self.assertEqual(User.select(id), 1)

        # testing the post request for user without name parameter
        self.app.post('/users', data=dict(first_name=' ',
                                          last_name='Snow',
                                          email='jon+1@snow',
                                          password='toto1234'))
        self.assertEqual(User.select(id), 2)

        # testing the post request for user without last_name parameter
        self.app.post('/users', data=dict(first_name='Jon',
                                          last_name=' ',
                                          email='jon+2@snow',
                                          password='toto1234'))
        # testing without and email
        self.app.post('/users', data=dict(first_name='Jon',
                                          last_name='b ',
                                          email=' ',
                                          password='toto1234'))
        self.assertEqual(User.select(id), 3)

        # testing without a password
        self.app.post('/users', data=dict(first_name='Jon',
                                          last_name='b',
                                          email='s@gmail.com ',
                                          password=' '))
        self.assertEqual(User.select(id), 4)

        # testing if an user can't have the same email
        email_test = self.app.post('/users', data=dict(first_name='Jon',
                                                       last_name='Snow',
                                                       email='jon@snow',
                                                       password='toto1234'))

        assert email_test.status_code == 409

    # def test_list(self):
    #    list_test = self.app.get('/users')
    #    print list_test.id
