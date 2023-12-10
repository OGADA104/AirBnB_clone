#!/usr/bin/python3
"""my review module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """review class """
    def __init__(self, *args, **kwargs):
        """initialise base model"""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

    def __str__(self):
        """ Return a string representation of the object """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            str(self.__dict__))
