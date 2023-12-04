#!/usr/bin/python3
"""
Module that defines BaseModel class.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Class that defines BaseModel logic.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for BaseModel class.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                if key in ["created_at", "updated_at"]:
                    self.__setattr__(key, datetime.fromisoformat(value))
                else:
                    self.__setattr__(key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Method that returns string representation of an instance.
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Method that updates the updated_at attribute of an instance.
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Method that returns dictionary representation an instance.
        """

        result = {"__class__": self.__class__.__name__}

        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                result[key] = value.isoformat("T")
            else:
                result[key] = value

        return result
