#!/usr/bin/python3
"""
Module used to define test cases for place class.
"""

from models.place import Place
from tests.test_models.test_basemodel import test_basemodel


class test_Place(test_basemodel):
    """class Implementation"""

    def __init__(self, *args, **kwargs):
        """__init__ Method"""

        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test city_id"""

        obj = self.value()
        self.assertEqual(type(obj.city_id), str)

    def test_user_id(self):
        """Test user_id"""

        obj = self.value()
        self.assertEqual(type(obj.user_id), str)

    def test_name(self):
        """Test name"""

        obj = self.value()
        self.assertEqual(type(obj.name), str)

    def test_description(self):
        """Test description"""

        obj = self.value()
        self.assertEqual(type(obj.description), str)

    def test_number_rooms(self):
        """Test number_rooms"""

        obj = self.value()
        self.assertEqual(type(obj.number_rooms), int)

    def test_number_bathrooms(self):
        """Test number_bathrooms"""

        obj = self.value()
        self.assertEqual(type(obj.number_bathrooms), int)

    def test_max_guest(self):
        """Test max_guest"""

        obj = self.value()
        self.assertEqual(type(obj.max_guest), int)

    def test_price_by_night(self):
        """Test price_by_night"""

        obj = self.value()
        self.assertEqual(type(obj.price_by_night), int)

    def test_latitude(self):
        """Test latitude"""

        obj = self.value()
        self.assertEqual(type(obj.latitude), float)

    def test_longitude(self):
        """Test longitude"""

        obj = self.value()
        self.assertEqual(type(obj.longitude), float)

    def test_amenity_ids(self):
        """Test amenity_ids"""

        obj = self.value()
        self.assertEqual(type(obj.amenity_ids), list)
