#!/usr/bin/python3
"""state module """
from models.base_model import BaseModel


class State(BaseModel):
    """class state model inheriting from basemodel"""

    def __init__(self):
        super().__init__()
        self.name = str()
