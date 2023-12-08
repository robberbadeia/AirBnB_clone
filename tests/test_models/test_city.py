#!/usr/bin/python3
"""
Module used to define test cases for city class.
"""

from models.city import City
from tests.test_models.test_basemodel import test_basemodel


class test_City(test_basemodel):
    """class Implementation"""

    def __init__(self, *args, **kwargs):
        """__init__ Method"""

        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_name(self):
        """Test name"""

        obj = self.value()
        self.assertEqual(type(obj.name), str)

    def test_state_id(self):
        """Test state_id"""

        obj = self.value()
        self.assertEqual(type(obj.state_id), str)
