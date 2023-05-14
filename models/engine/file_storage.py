#!/usr/bin/python3
"""This module defines FileStorage class"""


import json
import os.path
from models import base_model


BaseModel = base_model.BaseModel
classes = ['BaseModel']


class FileStorage:
    """Implements FilesStorage class that serialize to a JSON file
    and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary with all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with the key <obj class name>.id
        Args:
            obj(Object): Object
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        dic = {}
        for key, value in FileStorage.__objects.items():
            dic[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding='utf-8') as jsonfile:
            json.dump(dic, jsonfile)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8")\
                    as jsonfile:
                dict_objs = json.load(jsonfile)
                for key, value in dict_objs.items():
                    class_name = key.split(".")[0]
                    if class_name in classes:
                        FileStorage.__objects[key] = eval(class_name)(**value)
