#!/usr/bin/python3
"""This module defines the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Public class attr
        place_id (str) default=empty string: it will
            be the place.id
        user_id (str) default=empty string: it will
            be the user.id
        text (str) default=empty string:
    """
    place_id = ""
    user_id = ""
    text = ""
