from app import app
import unittest
import logging
import md5
# import json
from app.models.base import db
from app.models.user import User


class userTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        logging.disable(logging.CRITICAL)
        # connecting to database
        db.connect()
        db.create_tables([User])

    def tearDown(self):
        User.delete().execute()
        pass

    def test_create(self):
        new_user = User(first_name='Gonzalo',
                        last_name='Garcia',
                        email='gonzalo.garcia@garcia.com',
                        password=md5.new("password").hexdigest())
        new_user.save()
