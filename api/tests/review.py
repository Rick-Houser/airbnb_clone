import unittest
from app.models.base import db
from app.models.review import Review
from app.models.review_place import ReviewPlace
from app.models.review_user import ReviewUser
from app.models.user import User
from app.models.place import Place
from app.models.city import City
from app.models.state import State
from app import app
import logging
import json


class review_test(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        # logging.disable(logging.CRITICAL)
        # connectting to database
        db.connect()
        db.create_tables([User], safe=True)
        db.create_tables([State], safe=True)
        db.create_tables([City], safe=True)
        db.create_tables([Place], safe=True)
        db.create_tables([Review], safe=True)
        db.create_tables([ReviewUser], safe=True)
        db.create_tables([ReviewPlace], safe=True)
        # Creating a new users
        user1 = User(first_name='Jon',
                     last_name='Snow',
                     email='jon@snow',
                     password='toto1234')
        user1.save()

        user2 = User(first_name='Steven',
                     last_name='Garcia',
                     email='SG@snow',
                     password='toto1234')
        user2.save()

    def tearDown(self):
        # deleting tables
        db.drop_tables([ReviewPlace])
        db.drop_tables([ReviewUser])
        db.drop_tables([Review])
        db.drop_tables([Place])
        db.drop_tables([City])
        db.drop_tables([User])
        db.drop_tables([State])

    # def test_post(self):
    #     new_review = self.app.post('/users/1/reviews',
    #                                data=dict(message="I like it",
    #                                          stars=5))
    #     assert new_review.status_code == 200
    #     # check the id  of the review should be 1
    #     assert json.loads(new_review.data)['id'] == 1
    #     # creating a review by an user that does not exist
    #     new_review = self.app.post('/users/3/reviews',
    #                                data=dict(message="I like it",
    #                                          stars=5))
    #     assert new_review.status_code == 404

    def test_get(self):
        # creating a review by an user that exist
        new_review = self.app.post('/users/1/reviews',
                                   data=dict(message="I like it",
                                             stars=5))
        assert new_review.status_code == 200

        # getting a review for a user that does not exist
        get_review = self.app.get('/users/3/reviews')
        assert get_review.status_code == 404

        # getting a review for  user that does exist
        get_review = self.app.get('/users/1/reviews')
        assert get_review.status_code == 200
        # this user does have reviews
        # getting the number of json items
        assert len(json.loads(get_review.data)) == 0
        # # getting a review for  user that does exist but no reviews
        get_review = self.app.get('/users/2/reviews')
        assert get_review.status_code == 200
        # this user doesnt have reviews
        assert len(json.loads(get_review.data)) == 0


    # def test_get_review(self):
    #
    #     # creating a review by an user that exist
    #     new_review = self.app.post('/users/1/reviews',
    #                                data=dict(message="I like it",
    #                                          user_id=1,
    #                                          stars=5))
    #     assert new_review.status_code == 200
    #
    #     # getting a review for a user that does not exist
    #     get_review = self.app.get('/users/3/reviews/1')
    #     assert get_review.status_code == 404
    #
    #     # getting a review for a review that does not exist
    #     get_review = self.app.get('/users/1/reviews/5')
    #     assert get_review.status_code == 404
    #
    #     # getting a review for  user that does exist
    #     get_review = self.app.get('/users/1/reviews/1')
    #     assert get_review.status_code == 200
    #     # this user does have reviews
    #     assert len(get_review.data) > 0
    #     # getting a review for  user that does exist but no review
    #
    # def test_delete(self):
    #     # creating a review by an user that exist
    #     new_review = self.app.post('/users/1/reviews',
    #                                data=dict(message="I like it",
    #                                          user_id=1,
    #                                          stars=5))
    #     assert new_review.status_code == 200
    #
    #     # checking how many reviews there are before deleting
    #     get_review = self.app.get('/users/1/reviews/1')
    #     assert get_review.status_code == 200
    #     size_before = len(get_review.data)
    #
    #     # delition of a review that does not exist
    #     deleting_review = self.app.delete('/users/1/reviews/3')
    #     assert deleting_review.status_code == 404
    #
    #     # delition of a review that does not exist
    #     deleting_review = self.app.delete('/users/13/reviews/1')
    #     assert deleting_review.status_code == 404
    #
    #     # delition of a review that does not exist
    #     deleting_review = self.app.delete('/users/1/reviews/1')
    #     assert deleting_review.status_code == 200
    #
    #     # checking how many reviews there are after deleting
    #     get_review = self.app.get('/users/1/reviews/1')
    #     assert get_review.status_code == 200
    #     size_after = len(get_review.data)
    #
    #     # checking that the size is smaller after deleting
    #     assert size_after < size_before
    #
    # def test_review_place(self):
    #     # Creating a setUp
    #     new_state = State(name='California')
    #     new_state.save()
    #     new_city = City(name='San Francisco', state=1)
    #     new_city.save()
    #     new_place = Place(owner=1,
    #                       city=1,
    #                       name="Steven",
    #                       description="house",
    #                       number_rooms=3,
    #                       number_bathrooms=2,
    #                       max_guest=3,
    #                       price_by_night=100,
    #                       latitude=37.774929,
    #                       longitude=-122.419416)
    #     new_place.save()
    #     new_review = self.app.post('/places/1/reviews',
    #                                data=dict(message="I like it",
    #                                          user_id=1,
    #                                          stars=5))
    #     assert new_review.status_code == 200
    #
    #     # Getting a review for a place that does not exist
    #     get_review_place = self.app.get('/places/3/reviews')
    #     assert get_review_place == 404
    #
    #     # Getting a review for a place that does exist
    #     get_review_place = self.app.get('/places/1/reviews')
    #     assert get_review_place == 200
    #     # Checking that there is at least 1 review
    #     assert len(get_review_place.data) > 0
    #
    # def test_review_place2(self):
    #     # Creating a setUp
    #     new_state = State(name='California')
    #     new_state.save()
    #     new_city = City(name='San Francisco', state=1)
    #     new_city.save()
    #     new_place = Place(owner=1,
    #                       city=1,
    #                       name="Steven",
    #                       description="house",
    #                       number_rooms=3,
    #                       number_bathrooms=2,
    #                       max_guest=3,
    #                       price_by_night=100,
    #                       latitude=37.774929,
    #                       longitude=-122.419416)
    #     new_place.save()
    #
    #     # Creating a review for a place that exist
    #     new_review = self.app.post('/places/1/reviews',
    #                                data=dict(message="I like it",
    #                                          user_id=1,
    #                                          stars=5))
    #     assert new_review.status_code == 200
    #     # checking the review id, should be 1
    #     assert json.dumps(new_review.data)["id"] == 1
    #
    #     # Creating a review for a place that does not exist
    #     new_review = self.app.post('/places/3/reviews',
    #                                data=dict(message="I like it",
    #                                          user_id=1,
    #                                          stars=5))
    #     assert new_review.status_code == 404
    #
    # def test_review_place3(self):
    #     # Creating a setUp
    #     new_state = State(name='California')
    #     new_state.save()
    #     new_city = City(name='San Francisco', state=1)
    #     new_city.save()
    #     new_place = Place(owner=1,
    #                       city=1,
    #                       name="Steven",
    #                       description="house",
    #                       number_rooms=3,
    #                       number_bathrooms=2,
    #                       max_guest=3,
    #                       price_by_night=100,
    #                       latitude=37.774929,
    #                       longitude=-122.419416)
    #     new_place.save()
    #
    #     # Creating a review for a place that exist
    #     new_review = self.app.post('/places/1/reviews',
    #                                data=dict(message="I like it",
    #                                          user_id=1,
    #                                          stars=5))
    #     assert new_review.status_code == 200
    #
    #     # Checking for a review that does not exist
    #     new_review_get = self.app.get('/places/1/2')
    #     assert new_review_get.status_code == 404
    #
    #     # Checking for a place that does not exist
    #     new_review_get = self.app.get('/places/2/2')
    #     assert new_review_get.status_code == 404
    #
    #     # Checking for a review that does not exist
    #     new_review_get = self.app.get('/places/1/1')
    #     assert new_review_get.status_code == 200
    #
    # def test_delete2(self):
    #     # creating a review by an user that exist
    #     new_review = self.app.post('/places/1/reviews',
    #                                data=dict(message="I like it",
    #                                          user_id=1,
    #                                          stars=5))
    #     assert new_review.status_code == 200
    #
    #     # checking how many reviews there are before deleting
    #     get_review = self.app.get('/places/1/1')
    #     assert get_review.status_code == 200
    #     size_before = len(get_review.data)
    #
    #     # delition of a review that does not exist
    #     deleting_review = self.app.delete('/places/1/3')
    #     assert deleting_review.status_code == 404
    #
    #     # delition of a review that does not exist
    #     deleting_review = self.app.delete('/places/13/1')
    #     assert deleting_review.status_code == 404
    #
    #     # delition of a review that does not exist
    #     deleting_review = self.app.delete('/places/1/1')
    #     assert deleting_review.status_code == 200
    #
    #     # checking how many reviews there are after deleting
    #     get_review = self.app.get('/places/1/1')
    #     assert get_review.status_code == 200
    #     size_after = len(get_review.data)
    #
    #     # checking that the size is smaller after deleting
    #     assert size_after < size_before
