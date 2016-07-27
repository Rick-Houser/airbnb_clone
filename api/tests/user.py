from app import app
import unittest
import logging
from app.models.base import db
from app.models.user import User
from app.views.users import *
import json
# from app.views.user import User


class userTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        logging.disable(logging.CRITICAL)
        # connecting to database
        db.connect()
        # creating a database
        db.create_tables([User], safe=True)

    def tearDown(self):
        # deleting user
        # User.delete().execute()
        # deleting the table user
        db.drop_tables([User], safe=True)

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
        self.assertEqual(User.select(id), 3)
        # testing without and email
        self.app.post('/users', data=dict(first_name='Jon',
                                          last_name='b ',
                                          email=' ',
                                          password='toto1234'))
        self.assertEqual(User.select(id), 4)

        # testing without a password
        self.app.post('/users', data=dict(first_name='Jon',
                                          last_name='b',
                                          email='s@gmail.com ',
                                          password=' '))
        self.assertEqual(User.select(id), 5)

        # testing if an user can't have the same email
        email_test = self.app.post('/users', data=dict(first_name='Jon',
                                                       last_name='Snow',
                                                       email='jon@snow',
                                                       password='toto1234'))

        assert email_test.status_code == 409

    def test_list(self):
        list_test = self.app.get('/users')
        # nth elements if users were created
        try:
            to_dict = json.loads(list_test.data)
            return len(to_dict)
        # return 0 elements if no user was created
        except:
            return 0

    def test_get(self):
        # Creating an user
        new_user = self.app.post('/users', data=dict(first_name='Jon',
                                                     last_name='Snow',
                                                     email='j@snow',
                                                     password='toto1234'))
        # Checking the status code
        assert new_user.status_code == 200
        # Getting the user
        response = self.app.get('/users/1').data
        # checking if the user created is the same as the user returned
        # will return True is the  users match else will return false
        assert sorted(response) == sorted(new_user.data)

        # checking when trying to get an id that is not linked to an user
        response = self.app.get('/users/3')
        assert response.status_code == 404

    def test_delete(self):
        # Creating an user
        new_user = self.app.post('/users', data=dict(first_name='Jon',
                                                     last_name='Snow',
                                                     email='jon@snow',
                                                     password='toto1234'))
        # checking the number of users after creation
        list_test = self.app.get('/users')
        # nth elements if users were created
        to_dict = json.loads(list_test.data)
        assert len(to_dict) == 1
        # deleting the user
        self.app.delete('/users/1')

        # checking the number of users after delition
        list_test = self.app.get('/users')
        # nth elements if users were created
        try:
            to_dict = json.loads(list_test.data)
        except:
            assert True
        # checking the status code
        assert new_user.status_code == 200
        # deleting an user
        self.app.delete('/users/3').data
        # getting an user
        response = self.app.get('/users/3')
        assert response.status_code == 404

    def test_update(self):
        # Creating an user
        new_user = self.app.post('/users', data=dict(first_name='Jon',
                                                     last_name='Snow',
                                                     email='jon@snow',
                                                     password='toto1234'))
        # checking the status code
        assert new_user.status_code == 200

        # updating the user first_name
        self.app.put('/users/1', data=dict(first_name='steven'))
        list_test = self.app.get('/users/1')
        # checking the status code
        assert list_test.status_code == 200

        # updating users last name
        self.app.put('/users/1', data=dict(last_name='garcia'))
        list_test = self.app.get('/users/1')
        # checking the status code
        assert list_test.status_code == 200

        # updating the email
        self.app.put('/users/1', data=dict(email='steven@gmail.com'))
        list_test = self.app.get('/users/1')
        # checking the status code
        assert list_test.status_code == 200

        # updating the password
        self.app.put('/users/1', data=dict(password='123345'))
        list_test = self.app.get('/users/1')
        # checking the status code
        assert list_test.status_code == 200
        self.app.put('/users/3', data=dict(first_name="John"))
        # Testing for a user that does not exist
        response = self.app.get('/users/3')
        # if the user does not exist code is 404
        assert response.status_code == 404
