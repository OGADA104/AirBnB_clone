#!/usr/bin/python3
"""my review module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """review class """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
