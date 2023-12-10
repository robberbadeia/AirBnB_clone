#!/usr/bin/python3
"""
Module that defines unit tests for FileStorage class.
"""

import os
import json
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


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

        self.assertIsInstance(self.__class().all(), dict)

    def test_new(self):
        """
        Method that tests new method.
        """

        storage = self.__class()
        base_model = BaseModel()
        base_model.id = 1488
        storage.new(base_model)
        key = base_model.__class__.__name__ + "." + str(base_model.id)
        self.assertIn(key, storage.all())

    def test_save(self):
        """
        Method that tests save method.
        """

        storage = self.__class()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as f:
            self.assertEqual(json.load(f),
                             {k: v.to_dict() for k, v in storage.all().items()}
                             )

    def test_reload(self):
        """
        Method that tests reload method.
        """

        obj = BaseModel()
        with open("file.json", "w") as f:
            f.write("{ " + f'"BaseModel.{obj.id}": ' +
                    json.dumps(obj.to_dict()) + " }")

        storage = self.__class()
        storage.reload()

        self.assertIn(f"BaseModel.{obj.id}", storage.all())


if __name__ == "__main__":
    unittest.main()
