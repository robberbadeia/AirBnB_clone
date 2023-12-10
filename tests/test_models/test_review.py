#!/usr/bin/python3
"""
Module that defines unit tests for Review class.
"""

import unittest
from models.review import Review
from tests.test_models.test_base_model import TestBaseModel


class TestReview(TestBaseModel):
    """
    Class that defines unit tests for Review class.
    """

    __class = Review
    __class_name = "Review"

    def test_place_id(self):
        """
        Method that tests place_id attribute.
        """

        self.assertEqual(type(self.__class().place_id), str)

    def test_user_id(self):
        """
        Method that tests user_id attribute.
        """

        self.assertEqual(type(self.__class().user_id), str)

    def test_text(self):
        """
        Method that tests text attribute.
        """

        self.assertEqual(type(self.__class().text), str)


if __name__ == "__main__":
    unittest.main()
