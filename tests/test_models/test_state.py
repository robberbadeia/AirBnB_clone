#!/usr/bin/python3
"""
Module that defines unit tests for State class.
"""

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
        Method that tests updated_at attribute.
        """

        self.assertEqual(type(self.__class().name), str)
