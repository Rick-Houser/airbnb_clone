from app import app
import unittest
import json
from flask import jsonify


class Test(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_200(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_status(self):
        response = self.app.get('/')
        to_dict = json.loads(response.data)
        # checks if the json key status is equal to OK
        self.assertEqual(to_dict['status'],  "OK")

    # def test_time(self):

    # def test_time_utc(self):
