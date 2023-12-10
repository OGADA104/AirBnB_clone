#!/usr/bin/python3
"""state module """
from models.base_model import BaseModel


class State(BaseModel):
    """class state model inheriting from basemodel"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
