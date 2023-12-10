#!/usr/bin/python3
"""
Module that defines unit tests for FileStorage class.
"""

import os
import json
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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

        FileStorage._FileStorage__objects = {}

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

        b = BaseModel()
        u = User()
        s = State()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()

        storage.new(b)
        storage.new(u)
        storage.new(s)
        storage.new(c)
        storage.new(a)
        storage.new(p)
        storage.new(r)

        self.assertIn("BaseModel." + b.id, storage.all())
        self.assertIn(b, storage.all().values())
        self.assertIn("User." + u.id, storage.all())
        self.assertIn(u, storage.all().values())
        self.assertIn("State." + s.id, storage.all())
        self.assertIn(s, storage.all().values())
        self.assertIn("City." + c.id, storage.all())
        self.assertIn(c, storage.all().values())
        self.assertIn("Amenity." + a.id, storage.all())
        self.assertIn(a, storage.all().values())
        self.assertIn("Place." + p.id, storage.all())
        self.assertIn(p, storage.all().values())
        self.assertIn("Review." + r.id, storage.all())
        self.assertIn(r, storage.all().values())

    def test_save(self):
        """
        Method that tests save method.
        """

        storage = self.__class()

        b = BaseModel()
        u = User()
        s = State()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()

        storage.new(b)
        storage.new(u)
        storage.new(s)
        storage.new(c)
        storage.new(a)
        storage.new(p)
        storage.new(r)

        storage.save()

        with open("file.json", "r") as f:
            save = f.read()
            self.assertIn("BaseModel." + b.id, save)
            self.assertIn("User." + u.id, save)
            self.assertIn("State." + s.id, save)
            self.assertIn("City." + c.id, save)
            self.assertIn("Amenity." + a.id, save)
            self.assertIn("Place." + p.id, save)
            self.assertIn("Review." + r.id, save)

    def test_reload(self):
        """
        Method that tests reload method.
        """

        storage = self.__class()

        b = BaseModel()
        u = User()
        s = State()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()

        storage.new(b)
        storage.new(u)
        storage.new(s)
        storage.new(c)
        storage.new(a)
        storage.new(p)
        storage.new(r)

        storage.save()
        storage.reload()

        objects = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + b.id, objects)
        self.assertIn("User." + u.id, objects)
        self.assertIn("State." + s.id, objects)
        self.assertIn("Place." + p.id, objects)
        self.assertIn("City." + c.id, objects)
        self.assertIn("Amenity." + a.id, objects)
        self.assertIn("Review." + r.id, objects)


if __name__ == "__main__":
    unittest.main()
