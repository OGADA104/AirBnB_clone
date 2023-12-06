#!/usr/bin/python3
"""This module holds the class FileStorage"""
import json


class FileStorage():
    """Serializes instances to a JSON file
    and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dct = {key: value.to_dict() for key, value
               in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(dct, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                objs = json.load(f)
            for key, value in objs.items():
                cls_name = k.split('.')[0]
                obj = eval(cls_name + "(**v)")
                FileStorage.__objects[k] = obj
        except FileNotFoundError:
            pass
