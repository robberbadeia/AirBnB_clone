#!/usr/bin/python3
"""
Module used to define test cases for review class.
"""

from models.review import Review
from tests.test_models.test_basemodel import test_basemodel


class test_Review(test_basemodel):
    """class Implementation"""

    def __init__(self, *args, **kwargs):
        """__init__ Method"""

        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test place_id"""

        obj = self.value()
        self.assertEqual(type(obj.place_id), str)

    def test_user_id(self):
        """Test user_id"""

        obj = self.value()
        self.assertEqual(type(obj.user_id), str)

    def test_text(self):
        """Test text"""

        obj = self.value()
        self.assertEqual(type(obj.text), str)
