#!/usr/bin/python3
""" a base model for the air bnb project

    usage : "to be updated"
"""
import uuid
from datetime import datetime


class BaseModel:
    """class base model for airbnb"""

    def __init__(self, *args, **kwargs):
        """init method to class BaseModel"""
        for key in ("created_at", "updated_at"):
            if key in kwargs:
                kwargs[key] = datetime.strptime(
                        kwargs[key],
                        '%Y-%m-%dT%H:%M:%S.%f'
                        )
        self.id = kwargs.get("id", str(uuid.uuid4()))
        self.created_at = kwargs.get("created_at", datetime.now().isoformat())
        self.updated_at = kwargs.get("updated_at", datetime.now().isoformat())
        for key, value in kwargs.items():
            if key not in ("id", "created_at", "updated_at"):
                setattr(self, key, value)

    def save(self):
        """ saves the updated time"""
        from models import storage
        self.updated_at = datetime.now().isoformat()
        if hasattr(storage, 'new'):
            storage.new(self)
        storage.save()
        return self.updated_at

    def to_dict(self):
        """format dict instance"""
        base_dict = {key: value for key, value in self.__dict__.items()}
        for key, value in base_dict.items():
            if isinstance(value, datetime):
                base_dict[key] = value.isoformat()
        return base_dict

    def __str__(self):
        """ format class for print"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                str(self.__dict__))
