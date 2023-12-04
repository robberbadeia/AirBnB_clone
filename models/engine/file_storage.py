#!/usr/bin/python3
"""
Module that serializes instances to a JSON file and deserializes JSON file to instances.
"""
import json
from models.base_model import BaseModel

class FileStorage:
    """class implementation"""
    __file_path = "file.json"
    __objects = {}
    class_dic = {"BaseModel" : BaseModel}

    def all(self):
        """
        Method that returns the dictionary __objects.
        """

        return (self.__objects)
    
    def new(self, obj):
        """
        Method that sets in __objects the obj with key <obj class name>.id.
        """

        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Method that serializes __objects to the JSON file.
        """

        json_objects = {}
        for key, obj in self.__objects.items():
            json_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_objects, file)

    def reload(self):
        """
        Method that deserializes the JSON file to __objects.
        """

        try:
            with open(self.__file_path, 'r') as file:
                d = json.load(file)
            for k, v in d.items():
                obj = self.class_dic[v['__class__']](**v)
                self.__objects[k] = obj
        except FileNotFoundError:
            pass
        pass
