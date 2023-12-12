#!/usr/bin/python3
"""test module for base class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch
import uuid


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """initiate an instance"""
        self.base_model = BaseModel()

    def tearDown(self):
        """clean-up"""
        del self.base_model

    def test_instance_creation(self):
        """assert instance creation"""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertIsInstance(uuid.UUID(self.base_model.id), uuid.UUID)

    def test_save(self):
        """test save method"""
        initial_updated_at = self.base_model.updated_at
        with patch('models.storage') as mock_storage:
            self.base_model.save()
            updated_at_after_save = self.base_model.updated_at
            self.assertNotEqual(initial_updated_at, updated_at_after_save)
            mock_storage.save.assert_called_once()

    def test_to_dict(self):
        """test to dict"""
        self.base_model.name = "Test Name"
        self.base_model.number = 42

        obj_dict = self.base_model.to_dict()

        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('name', obj_dict)
        self.assertIn('number', obj_dict)

        self.assertIsInstance(datetime.strptime(obj_dict['created_at'],
            '%Y-%m-%dT%H:%M:%S.%f'),
            datetime)
        self.assertIsInstance(datetime.strptime(obj_dict['updated_at'],
            '%Y-%m-%dT%H:%M:%S.%f'),
            datetime)

    def test_str(self):
        """test __str__"""
        string_representation = str(self.base_model)
        self.assertIn('BaseModel', string_representation)
        self.assertIn(str(self.base_model.id), string_representation)


if __name__ == '__main__':
    unittest.main()
