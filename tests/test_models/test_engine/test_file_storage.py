#!/usr/bin/python3
"""
Module to test FileStorage class
"""

import unittest
import os
from models.engine.file_storage import FileStorage


class TestStorage(unittest.TestCase):
    """
    Class that defines unit tests for File_storage class.
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
        """Method that tests all method"""

        instance = self.__class()
        inst_dict = instance.all()
        self.assertIsNotNone(inst_dict)
        self.assertEqual(type(inst_dict), dict)
