import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def tearDown(self):
        del self.user

    def test_inheritance(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_attributes_types(self):
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_str_method(self):
        string_representation = str(self.user)
        self.assertIn('User', string_representation)
        self.assertIn(str(self.user.id), string_representation)

    def test_created_at_and_updated_at(self):
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_to_dict_method(self):
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        obj_dict = self.user.to_dict()

        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('email', obj_dict)
        self.assertIn('password', obj_dict)
        self.assertIn('first_name', obj_dict)
        self.assertIn('last_name', obj_dict)

        self.assertIsInstance(
            datetime.strptime(obj_dict['created_at'], '%Y-%m-%dT%H:%M:%S.%f'),
            datetime)
        self.assertIsInstance(
            datetime.strptime(obj_dict['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'),
            datetime)


if __name__ == '__main__':
    unittest.main()
