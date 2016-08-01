from app import app
from app.models.base import db
from app.models.city import City
from app.models.state import State
from app.models.place import Place
from app.models.place_book import PlaceBook
import unittest
import logging
from app.models.user import User


class place_book_test(unittest.TestCase):
    def setUp(self):
        # disabling logs
        logging.disable(logging.CRITICAL)
        self.app = app.test_client()
        # connecting to the database
        db.connect()
        # creating tables
        db.create_tables([User], safe=True)
        db.create_tables([State], safe=True)
        db.create_tables([City], safe=True)
        db.create_tables([Place], safe=True)
        db.create_tables([PlaceBook], safe=True)

        # Creating a setUp
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

    def tearDown(self):
        # deleting database
        db.drop_tables([PlaceBook])
        db.drop_tables([Place])
        db.drop_tables([City])
        db.drop_tables([State])
        db.drop_tables([User])

    def test_create(self):
        # Creating a new book for a place
        new_book = self.app.post('/places/1/books',
                                 data=dict(user_id=1,
                                           date_start="2016-05-01 12:00:00",
                                           number_nights=5))
        assert new_book.status_code == 200

        # Creating a new book for a place that does not exist
        new_book = self.app.post('/places/5/books',
                                 data=dict(user_id=1,
                                           date_start="2016-05-01 12:00:00",
                                           number_nights=5))
        assert new_book.status_code == 404

        # Getting a book from a place that exist
        get_book = self.app.get('/places/1/books')
        assert get_book.status_code == 200

        # Getting a book from a place that exist
        get_book = self.app.get('/places/5/books')
        assert get_book.status_code == 404

        # Getting a booking for a place and booking that exist
        get_place_book = self.app.get('places/1/books/1')
        assert get_place_book.status_code == 200

        # Getting a booking for a place that does not exist
        get_place_book = self.app.get('places/2/books/1')
        assert get_place_book.status_code == 404

        # Getting a booking that does not exist
        get_place_book = self.app.get('places/1/books/2')
        assert get_place_book.status_code == 404

        # updating the date
        get_update = self.app.put('/places/1/books/1',
                                  data=dict(date_start="2016-05-07 12:00:00"))
        assert get_update.status_code == 200

        # Updating the number of nights
        get_update = self.app.put('/places/1/books/1',
                                  data=dict(number_nights=2))
        assert get_update.status_code == 200

        # Updating is_validated
        get_update = self.app.put('/places/1/books/1',
                                  data=dict(is_validated=True))
        assert get_update.status_code == 200

        # Updating User
        get_update = self.app.put('/places/1/books/1',
                                  data=dict(user_id=2))
        assert get_update.status_code == 405

        # Deleing a booking for a place that exist
        book_delete = self.app.delete('/places/1/books/1')
        assert book_delete.status_code == 200

        # Deleing a booking for a place that does not exist
        book_delete = self.app.delete('/places/3/books/1')
        assert book_delete.status_code == 404

        # Deleing a booking that does not exist
        book_delete = self.app.delete('/places/1/books/5')
        assert book_delete.status_code == 404
