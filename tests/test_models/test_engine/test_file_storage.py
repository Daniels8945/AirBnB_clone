#!/usr/bin/python3
"""
"""

import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageInstatiation(unittest.TestCase):
    """
    """
    def test_FileStorage_inst_noargs(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_inst_withargs(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_initial(self):
        self.assertEqual(type(models.storage), FileStorage)

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_file.json"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_storage_returns_dict(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        objec = BaseModel()
        models.storage.new(objec)
        self.assertIn("BaseModel.{}".format(objec.id), models.storage.all())

    def test_new_withargs(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_and_reload(self):
        objec_1 = BaseModel()
        objec_2 = BaseModel()
        models.storage.new(objec_1)
        models.storage.new(objec_2)
        models.storage.save()

        store_new = FileStorage()
        store_new.reload()
        self.assertTrue(store_new.all().get("BaseModel.{}".format(objec_1.id) is not None))
        self.assertTrue(store_new.all().get("BaseModel.{}".format(objec_2.id) is not None))

    def test_save_to_file(self):
        objec = BaseModel()
        models.storage.new(objec)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_relaod_empty_f(self):
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()

if __name__ == "__main__":
    unittest.main()
