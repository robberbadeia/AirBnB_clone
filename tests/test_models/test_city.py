#!/usr/bin/python3
"""
Module that defines unit tests for City class.
"""

import unittest
from models.city import City
from tests.test_models.test_base_model import TestBaseModel


class TestCity(TestBaseModel):
    """
    Class that defines unit tests for City class.
    """

    __class = City
    __class_name = "City"

    def test_name(self):
        """
        Method that tests name attribute.
        """

        self.assertEqual(type(self.__class().name), str)

    def test_state_id(self):
        """
        Method that tests state_id attribute.
        """

        self.assertEqual(type(self.__class().state_id), str)


if __name__ == "__main__":
    unittest.main()
