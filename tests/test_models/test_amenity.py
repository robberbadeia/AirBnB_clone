#!/usr/bin/python3
"""
Module that defines unit tests for Amenity class.
"""

from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel


class TestAmenity(TestBaseModel):
    """
    Class that defines unit tests for Amenity class.
    """

    __class = Amenity
    __class_name = "Amenity"

    def test_name(self):
        """
        Method that tests name attribute.
        """

        self.assertEqual(type(self.__class().name), str)
