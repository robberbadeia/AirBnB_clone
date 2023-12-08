#!/usr/bin/python3
"""
Module used to define test cases for state class.
"""

from models.state import State
from tests.test_models.test_basemodel import test_basemodel


class test_User(test_basemodel):
    """class Implementation"""

    def __init__(self, *args, **kwargs):
        """__init__ Method"""

        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """Test name"""

        obj = self.value()
        self.assertEqual(type(obj.name), str)
