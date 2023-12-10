#!/usr/bin/python3
"""
Module that defines unit tests for Place class.
"""

import unittest
from models.place import Place
from tests.test_models.test_base_model import TestBaseModel


class TestPlace(TestBaseModel):
    """
    Class that defines unit tests for Place class.
    """

    __class = Place
    __class_name = "Place"

    def test_city_id(self):
        """
        Method that tests city_id attribute.
        """

        self.assertEqual(type(self.__class().city_id), str)

    def test_user_id(self):
        """
        Method that tests user_id attribute.
        """

        self.assertEqual(type(self.__class().user_id), str)

    def test_name(self):
        """
        Method that tests name attribute.
        """

        self.assertEqual(type(self.__class().name), str)

    def test_description(self):
        """
        Method that tests description attribute.
        """

        self.assertEqual(type(self.__class().description), str)

    def test_number_rooms(self):
        """
        Method that tests number_rooms attribute.
        """

        self.assertEqual(type(self.__class().number_rooms), int)

    def test_number_bathrooms(self):
        """
        Method that tests number_bathrooms attribute.
        """

        self.assertEqual(type(self.__class().number_bathrooms), int)

    def test_max_guest(self):
        """
        Method that tests max_guest attribute.
        """

        self.assertEqual(type(self.__class().max_guest), int)

    def test_price_by_night(self):
        """
        Method that tests price_by_night attribute.
        """

        self.assertEqual(type(self.__class().price_by_night), int)

    def test_latitude(self):
        """
        Method that tests latitude attribute.
        """

        self.assertEqual(type(self.__class().latitude), float)

    def test_longitude(self):
        """
        Method that tests longitude attribute.
        """

        self.assertEqual(type(self.__class().longitude), float)

    def test_amenity_ids(self):
        """
        Method that tests amenity_ids attribute.
        """

        self.assertEqual(type(self.__class().amenity_ids), list)


if __name__ == "__main__":
    unittest.main()
