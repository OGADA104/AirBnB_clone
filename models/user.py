#!/usr/bin/python3
"""user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """my user class that inherits from BaseModel"""
    email = str()
    password = str()
    first_name = str()
    last_name = str()
