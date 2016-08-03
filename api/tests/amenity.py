from app import app
from app.models.base import db
from app.models.amenity import Amenity
import unittest
import logging


class AmenitiesTest(unittest.TestCase):
	'''
	Disable logging calls with levels less severe than or equal to CRITICAL.
	connect to database and create table for testing.
	'''
    def setUp(self):
		logging.disable(logging.CRITICAL)
        self.app = app.test_client()

        db.connect()
        db.create_table([Amenity], safe=True)

	# Drop test table
	def tearDown(self):
		db.drop_table([Amenity], safe=True)

	# Create new amenity
    def test_post(self):
        new_amenity = self.app.post('/amenities', data=dict(name='amenity1'))
        assert new_amenity.status_code == 200

	# Get newly created amenity. 404 (Not Found) if amenity doesn't exist.
	def test_get(self):
		get_amenity = self.app.get('/amenities/1', data=dict(name='amenity1'))
        assert new_amenity.status_code == 200

		get_invalid_amenity = self.app.get('/amenities/9', data=dict(name='amenity1'))
        assert new_amenity.status_code == 404

	# Delete newly created amenity. 404 (Not Found) if amenity doesn't exist.
	def test_delete(self):
		get_amenity = self.app.delete('/amenities/1', data=dict(name='amenity1'))
        assert new_amenity.status_code == 200

		get_amenity = self.app.delete('/amenities/9', data=dict(name='amenity1'))
        assert new_amenity.status_code == 404
