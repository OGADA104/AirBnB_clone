#!/usr/bin/python3
"""test file storage"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import os
import json


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = 'test_file.json'
        self.file_storage = FileStorage()
        self.file_storage._FileStorage__file_path = self.file_path
        self.obj1 = BaseModel()
        self.obj2 = User()
        self.obj3 = State()

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all_method(self):
        all_objects = self.file_storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, {})

    def test_new_method(self):
        self.file_storage.new(self.obj1)
        self.file_storage.new(self.obj2)
        all_objects = self.file_storage.all()
        self.assertEqual(len(all_objects), 2)
        self.assertIn('BaseModel.' + self.obj1.id, all_objects)
        self.assertIn('User.' + self.obj2.id, all_objects)

    def test_save_method(self):
        self.file_storage.new(self.obj1)
        self.file_storage.new(self.obj2)
        self.file_storage.save()
        self.assertTrue(os.path.exists(self.file_path))

        with open(self.file_path, 'r') as file:
            data = json.load(file)
            self.assertIn('BaseModel.' + self.obj1.id, data)
            self.assertIn('User.' + self.obj2.id, data)

    def test_reload_method(self):
        self.file_storage.new(self.obj1)
        self.file_storage.new(self.obj2)
        self.file_storage.save()
        new_file_storage = FileStorage()
        new_file_storage._FileStorage__file_path = self.file_path
        new_file_storage.reload()
        all_objects = new_file_storage.all()
        self.assertEqual(len(all_objects), 2)
        self.assertIn('BaseModel.' + self.obj1.id, all_objects)
        self.assertIn('User.' + self.obj2.id, all_objects)

    def test_reload_method_nonexistent_file(self):
        nonexistent_path = 'nonexistent_file.json'
        self.file_storage._FileStorage__file_path = nonexistent_path
        self.file_storage.reload()
        all_objects = self.file_storage.all()
        self.assertEqual(all_objects, {})


if __name__ == '__main__':
    unittest.main()
