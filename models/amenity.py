#!/usr/bin/python3
"""amenity module """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """usage Amenity(str)"""

    def __init__(self, *args, **kwargs):
        """initiatilse from base model"""
        super().__init__(*args, **kwargs)
        self.name = ""
