#!/usr/bin/python3
"""city module"""
from models.base_model import BaseModel


class City(BaseModel):
    """usage city <string>"""
    def __init__(self):
        super().__init__()
        self.state_id = str()
        self.name = str()
