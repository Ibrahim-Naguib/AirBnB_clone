#!/usr/bin/python3
"""This module defines a class FileStorage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initialize a new FileStorage"""

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Args:
            obj (BaseModel): An instance of BaseModel
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        all_objects = FileStorage.__objects
        objects_dict = {}
        for key in all_objects.keys():
            objects_dict[key] = all_objects[key].to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(objects_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                object_dict = json.load(f)
                for obj in object_dict.values():
                    cls_name = obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
