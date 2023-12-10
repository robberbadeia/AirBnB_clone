#!/usr/bin/python3
"""
Module that defines unit tests for FileStorage class.
"""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.city import City


class TestFileStorage(unittest.TestCase):
    """
    Class that defines unit tests for FileStorage class.
    """

    __class = FileStorage
    __class_name = "FileStorage"

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

    def test_all(self):
        """
        Method that tests all method.
        """

        self.assertEqual(type(self.__class().all()), dict)

    def test_new(self):
        """
        Method that tests new method.
        """

        storage = self.__class()
        city = City()
        city.id = 1488
        storage.new(city)
        key = city.__class__.__name__ + "." + str(city.id)
        self.assertIsNotNone(storage.all()[key])


if __name__ == "__main__":
    unittest.main()
