#!/usr/bin/python3
"""
Module that defines unit tests for BaseModel class.
"""

import os
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Class that defines unit tests for BaseModel class.
    """

    __class = BaseModel
    __class_name = "BaseModel"

    def setUp(self):
        """
        Method that sets up environment before each test.
        """

    def tearDown(self):
        """
        Method that cleans up environment after each test.
        """

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_id(self):
        """
        Method that tests id attribute.
        """

        self.assertIsInstance(self.__class().id, str)

    def test_created_at(self):
        """
        Method that tests created_at attribute.
        """

        self.assertIsInstance(self.__class().created_at, datetime)

    def test_updated_at(self):
        """
        Method that tests updated_at attribute.
        """

        self.assertIsInstance(self.__class().updated_at, datetime)

    def test_str(self):
        """
        Method that tests __str__ method.
        """

        obj = self.__class()
        self.assertEqual(
            str(obj), f"[{self.__class_name}] ({obj.id}) {obj.__dict__}"
            )

    def test_save(self):
        """
        Method to test save method.
        """

        obj = self.__class()
        original_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(original_updated_at, obj.updated_at)
        self.assertTrue(os.path.isfile("file.json"))

    def test_to_dict(self):
        """
        Method that tests to_dict method.
        """

        obj = self.__class().to_dict()
        self.assertIsInstance(obj, dict)
        self.assertIn("__class__", obj)
        self.assertIsInstance(obj["created_at"], str)
        self.assertIsInstance(obj["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
