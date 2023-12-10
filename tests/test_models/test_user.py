#!/usr/bin/python3
"""
Module that defines unit tests for User class.
"""

import unittest
from models.user import User
from tests.test_models.test_base_model import TestBaseModel


class TestUser(TestBaseModel):
    """
    Class that defines unit tests for User class.
    """

    __class = User
    __class_name = "User"

    def test_first_name(self):
        """
        Method that tests first_name attribute.
        """

        self.assertEqual(type(self.__class().first_name), str)

    def test_last_name(self):
        """
        Method that tests last_name attribute.
        """

        self.assertEqual(type(self.__class().last_name), str)

    def test_email(self):
        """
        Method that tests email attribute.
        """

        self.assertEqual(type(self.__class().email), str)

    def test_password(self):
        """
        Method that tests password attribute.
        """

        self.assertEqual(type(self.__class().password), str)


if __name__ == "__main__":
    unittest.main()
