#!/usr/bin/python3
""" a base model for the air bnb project

    usage : "to be updated"
"""
import uuid
from datetime import datetime
form models import storage


class BaseModel:
    """class base model for airbnb"""

    def __init__(self, *args, **kwargs):
        """init method to class BaseModel"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()
            storage.new(self)

    def save(self):
        """ saves the updated time"""
        self.updated_at = datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        """format dict instance"""
        base_dict = {key: value for key, value in self.__dict__.items()}
        return base_dict

    def __str__(self):
        """ format class for print"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__)


if __name__ == "__main__":
    a = BaseModel()
    print(a.to_dict())
