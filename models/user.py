#!/usr/bin/python3
"""user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """my user class"""
    def __init__(self, *args, **kwargs):
        """initislize user class"""
        super().__init__(*args, **kwargs)
        self.email = str()
        self.password = str()
        self.first_name = str()
        self.last_name = str()

    def __str__(self):
        """ Return a string representation of the object """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            str(self.__dict__))


if __name__ == "__main__":
    my_user = User()
    print(my_user)
