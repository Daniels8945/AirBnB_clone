#!/usr/bin/python3
"""Unittest module for the BaseModel Class"""

import os
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """
        """
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        """
        """
        our_model = BaseModel()
        self.assertIsNotNone(our_model.id)
        self.assertIsNotNone(our_model.created_at)
        self.assertIsNotNone(our_model.updated_at)

    def test_str(self):
        """
        """
        our_model = BaseModel()
        self.assertTrue(str(our_model).startswith('[BaseModel]'))
        self.assertIn(our_model.id, str(our_model))
        self.assertIn(str(our_model.__dict__), str(our_model))

    def test_save(self):
        """
        """
        our_model = BaseModel()
        init_updated_at = our_model.updated_at
        curr_updated_at = our_model.save()
        self.assertNotEqual(init_updated_at, curr_updated_at)

    def test_to_dict(self):
        """
        """
        our_model = BaseModel()
        our_model_dict = our_model.to_dict()
        self.assertIsInstance(our_model_dict, dict)
        self.assertEqual(our_model_dict['created_at'], our_model.created_at.isoformat())
        self.assertEqual(our_model_dict['updated_at'], our_model.updated_at.isoformat())
        self.assertEqual(our_model_dict['__class__'], 'BaseModel')
        self.assertEqual(our_model_dict['id'], our_model.id)

if __name__ == '__main__':
    unittest.main()
