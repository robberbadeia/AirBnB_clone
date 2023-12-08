#!/usr/bin/python3
"""
Module to test BaseModel Class
"""

from models.base_model import BaseModel
import unittest
from datetime import datetime
import os


class test_basemodel(unittest.TestCase):
    """Class Implementation"""

    def __init__(self, *args, **kargs):
        """__init__ Method"""

        super().__init__(*args, **kargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def test_class_type(self):
        """Method to test class type"""

        inst = self.value()
        self.assertEqual(type(inst), BaseModel)

    def test_id(self):
        """Method to test id attribute type"""

        inst = self.value()
        self.assertEqual(type(inst.id), str)

    def test_created_at(self):
        """Method to test created_at attribute type"""

        inst = self.value()
        self.assertEqual(type(inst.created_at), datetime)

    def test_updated_at(self):
        """Method to test updated_at attribute type"""

        inst = self.value()
        self.assertEqual(type(inst.updated_at), datetime)

    def remove_json_file():
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_dict(self):
        """Method to test to_dict method"""

        inst = self.value()
        d = inst.to_dict()
        self.assertEqual(type(d), dict)

    def test_str(self):
        """Method to test __str__ method"""

        inst = self.value()
        self.assertEqual(
            str(inst), f'[{self.name}] ({inst.id}) {inst.__dict__}'
            )

    def test_save_one(self):
        """Method to test save method - Checking update_at atteribute"""

        inst = self.value()
        updated_at_1 = inst.updated_at
        inst.save()
        updated_at_2 = inst.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_save_two(self):
        """Method to test save method - Checking update_at is
            greater than created_at atteribute
        """

        inst = self.value()
        inst.save()
        updated_at_2 = inst.updated_at
        self.assertGreater(updated_at_2, inst.created_at)

    def test_save_three(self):
        """Method to test save method - checking the file 'file.json exists'"""

        inst = self.value()
        inst.save()
        os.path.isfile('file.json')
