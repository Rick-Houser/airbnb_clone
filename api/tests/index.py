from app import app
import unittest
import json
from datetime import datetime


class Root_Test(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_200(self):
        # getting the root path of my website
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_status(self):
        response = self.app.get('/')
        to_dict = json.loads(response.data)
        # checks if the json key status is equal to OK
        self.assertEqual(to_dict['status'],  "OK")

    def test_time(self):
        time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        response = self.app.get('/')
        # converting from json to dict
        to_dict = json.loads(response.data)
        self.assertEqual(to_dict['time'], time)

    def test_time_utc(self):
        utc_time = datetime.utcnow().strftime('%d/%m/%Y %H:%M:%S')
        response = self.app.get('/')
        to_dict = json.loads(response.data)
        self.assertEqual(to_dict['utc_time'], utc_time)
