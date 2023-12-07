#!/usr/bin/python3
"""
Module that defines FileStorage class.
"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Class that FileStorage logic.
    """

    __file_path = "file.json"
    __objects = {}
    __classes = {
        "BaseModel": BaseModel,
        "User": User
    }

    def all(self):
        """
        Method that returns the dictionary __objects.
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        Method that sets in __objects the obj with key <obj class name>.id.
        """

        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """
        Method that serializes __objects to the JSON file.
        """

        json_objects = {}

        for key, obj in FileStorage.__objects.items():
            json_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(json_objects, file)

    def reload(self):
        """
        Method that deserializes the JSON file to __objects.
        """

        try:
            with open(FileStorage.__file_path, "r") as file:
                d = json.load(file)

            for k, v in d.items():
                obj = FileStorage.__classes[v["__class__"]](**v)
                FileStorage.__objects[k] = obj
        except FileNotFoundError:
            pass

    def classes(self):
        """
        Method that returns the classes dictionary.
        """

        return FileStorage.__classes
