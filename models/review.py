#!/usr/bin/python3
"""my review module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """review class """
    def __init__(self):
        super().__init__()
        self.place_id = ""
        self.user_id = ""
        self.text = ""
