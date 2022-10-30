#!/usr/bin/env python3
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity
import os
"""
File storage engine for storing data
"""


class FileStorage:
    """
    store dcitionary object in a file engine database
    Args:
        __file_path ->str: file path to the file database
        __objects ->dict: dictionary objets store in the file
        database
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        set new in __objects new object value
        """
        new_object = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[new_object] = obj

    def save(self):
        """
        serialize objects to json file
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        try:
            with open(self.__file_path, mode="w", encoding="utf-8") as file:
                json.dump(obj=new_dict, fp=file)
        except FileNotFoundError:
            pass

    def reload(self):
        """
        deserialise json to objects if the file exit
        """
        if os.path.isfile(self.__file_path):
            file = open(file=self.__file_path, mode="r", encoding="utf-8")
            new_dict = json.load(fp=file)
            for key, value in new_dict.items():
                obj_class_name = key.split(sep=".")[0]
                FileStorage.__objects[key] = eval(obj_class_name)(**value)
            file.close()
