#!/usr/bin/python3
"""state module """
from models.base_model import BaseModel


class State(BaseModel):
    """class state model inheriting from basemodel"""

    def __init__(self, *args, **kwargs):
        """initialise state from base model"""
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        """ Return a string representation of the object """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            str(self.__dict__))
