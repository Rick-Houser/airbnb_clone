# import os
# from flask import Flask
from app import app
import unittest
# import urllib2


class Test(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        # flaskr.init_db()

    @app.route('/')
    def test_200(self):
        response = self.app.get('/')
        assert '200' in response.data

    def test_status(self):
        response = self.app.get('/')
        assert 'OK' in response.data

    # def test_time(self):

    # def test_time_utc(self):
