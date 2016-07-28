import unittest
from app.models.base import db
from app.models.review import Review
from app.models.user import User
from app import app
import logging
import json


class review_test(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        logging.disable(logging.CRITICAL)
        # connectting to database
        db.connect()
        db.create_tables([User], safe=True)
        db.create_tables([Review], safe=True)

    def tearDown(self):
        # deleting table
        db.drop_tables([Review])
        db.drop_tables([User])

    def test_post(self):
        # Creating a new user
        new_user = self.app.post('/users', data=dict(first_name='Jon',
                                                     last_name='Snow',
                                                     email='jon@snow',
                                                     password='toto1234'))
        assert new_user.status_code == 200
        # creating a review by an user that exist
        new_review = self.app.post('/users/1/reviews',
                                   data=dict(message="I like it",
                                             user_id=1,
                                             stars=5))
        assert new_review.status_code == 200
        # check the id  of the review should be 1
        assert json.dumps(new_review.data)['id'] == 1
        # creating a review by an user that does not exist
        new_review = self.app.post('/users/2/reviews',
                                   data=dict(message="I like it",
                                             user_id=1,
                                             stars=5))
        assert new_review.status_code == 404

    def test_get(self):
        # Creating a new user
        new_user = self.app.post('/users', data=dict(first_name='Jon',
                                                     last_name='Snow',
                                                     email='jon@snow',
                                                     password='toto1234'))
        assert new_user.status_code == 200
        #creating another user
        new_user2 = self.app.post('/users', data=dict(first_name='Jon',
                                                      last_name='Snow',
                                                      email='jon@snow',
                                                      password='toto1234'))
        assert new_user2.status_code == 200
        # creating a review by an user that exist
        new_review = self.app.post('/users/1/reviews',
                                   data=dict(message="I like it",
                                             user_id=1,
                                             stars=5))
        assert new_review.status_code == 200
        # check the id  of the review should be 1
        assert json.dumps(new_review.data)['id'] == 1
        # creating a review by an user that does not exist
        new_review = self.app.post('/users/2/reviews',
                                   data=dict(message="I like it",
                                             user_id=1,
                                             stars=5))
        assert new_review.status_code == 404
        # getting a review for a user that does not exist
        get_review = self.app.get('/users/3/reviews')
        assert get_review.status_code == 404

        # getting a review for  user that does exist
        get_review = self.app.get('/users/1/reviews')
        assert get_review.status_code == 200
        # this user does have reviews
        assert len(get_review.data) > 0
        # getting a review for  user that does exist but no review
        get_review = self.app.get('/users/2/reviews')
        assert get_review.status_code == 200
        # this user doesnt have reviews
        assert len(get_review.data) == 0
