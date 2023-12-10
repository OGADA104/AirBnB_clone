#!/usr/bin/python3
""" a base model for the air bnb project

    usage : "to be updated"
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """class base model for airbnb"""

    def __init__(self, *args, **kwargs):
        """init method to class BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(
                        kwargs[key],
                        '%Y-%m-%dT%H:%M:%S.%f'
                        )
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """ saves the updated time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """format dict instance"""
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = self.__class__.__name__
        base_dict["created_at"] = self.created_at.isoformat()
        base_dict["updated_at"] = self.updated_at.isoformat()
        return base_dict

    def __str__(self):
        """ format class for print"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__)
