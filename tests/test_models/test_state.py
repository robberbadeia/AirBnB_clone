#!/usr/bin/python3
"""
Module that defines unit tests for State class.
"""

import unittest
from models.state import State
from tests.test_models.test_base_model import TestBaseModel


class TestState(TestBaseModel):
    """
    Class that defines unit tests for State class.
    """

    __class = State
    __class_name = "State"

    def test_name(self):
        """
        Method that tests name attribute.
        """

        self.assertEqual(type(self.__class().name), str)


if __name__ == "__main__":
    unittest.main()
