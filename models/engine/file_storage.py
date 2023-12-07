#!/usr/bin/python3
""" file storage module"""
import json
import os


class FileStorage:
    """ file stogare class"""
    def __init__(self):
        """init method on file storage"""
        self.__file_path = 'file.json'
        print("File path:", os.path.abspath(self.__file_path))
        self.__objects = {}

    def all(self):
        """returns _dict objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        return self.__objects

    def save(self):
        """save to file"""
        if self.__file_path:
            mode = 'a' if os.path.exists(self.__file_path) else 'w'
            with open(self.__file_path, mode) as file:
                objects_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
                json.dump(objects_dict, file)

    def reload(self):
        """reload from file"""
        if self.__file_path:
            try:
                with open(self.__file_path, 'r') as file:
                    self.__objects = json.load(file)
                    for key, obj_dict in objects_dict.items():
                        class_name, obj_id = key.split('.')
                        obj = globals()[class_name].from_dict(obj_dict)
                        self.__objects[key] = obj
            except FileNotFoundError:
                pass
        else:
            pass
