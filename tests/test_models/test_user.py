#!/usr/bin/python3
"""
Module used to define test cases for user class.
"""

from models.user import User
from tests.test_models.test_basemodel import test_basemodel


class test_User(test_basemodel):
    """class Implementation"""

    def __init__(self, *args, **kwargs):
        """__init__ Method"""

        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test first name"""

        obj = self.value()
        self.assertEqual(type(obj.first_name), str)

    def test_last_name(self):
        """Test last name"""

        obj = self.value()
        self.assertEqual(type(obj.last_name), str)

    def test_email(self):
        """Test email"""

        obj = self.value()
        self.assertEqual(type(obj.email), str)

    def test_password(self):
        """Test password"""

        obj = self.value()
        self.assertEqual(type(obj.password), str)
