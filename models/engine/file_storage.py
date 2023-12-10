#!/usr/bin/python3
""" file storage module"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """ file stogare class"""
    def __init__(self):
        """init method on file storage"""
        self.__file_path = 'file.json'
        self.__objects = dict()

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
            with open(self.__file_path, 'w') as file:
                objects_dict = {
                        key: obj.to_dict()
                        for key,
                        obj in self.__objects.items()}
                json.dump(objects_dict, file)

    def reload(self):
        """reload from file"""
        if self.__file_path:
            try:
                with open(self.__file_path, 'r') as file:
                    objects_dict = json.load(file)
                    for key, obj_dict in objects_dict.items():
                        class_name, obj_id = key.split('.')
                        if class_name == "BaseModel":
                            obj = BaseModel(**obj_dict)
                        elif class_name == "User":
                            obj = User(**obj_dict)
                        elif class_name == "State":
                            obj = State(**obj_dict)
                        elif class_name == "City":
                            obj = City(**obj_dict)
                        elif class_name == "Amenity":
                            obj = Amenity(**obj_dict)
                        elif class_name == "Place":
                            obj = Place(**obj_dict)
                        elif class_name == "Review":
                            obj = Review(**obj_dict)
                        else:
                            continue
                        self.__objects[key] = obj
            except FileNotFoundError:
                pass
        else:
            pass
