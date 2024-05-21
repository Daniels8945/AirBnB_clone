#!/usr/bin/python3
"""Unittest module for the Amenity Class"""

import os
import unittest
import models
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_amenity_str_rep(self):
        amenity_test = Amenity()
        amenity_test.name = "Wifi"
        str_amenity = str(amenity_test)
        self.assertIn("Amenity", str_amenity)
        self.assertIn("Wifi", str_amenity)

    def test_amenity_attr(self):
        amenity_test = Amenity()
        self.assertEqual(amenity_test.name, "")

    def test_amenity_inherits_from_basemodel(self):
        amenity_test = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_to_dict(self):
        amenity_test = Amenity()
        amenity_test.name = "Wifi"
        amenity_test.save()
        dic_amenity = amenity_test.to_dict()
        self.assertEqual(dic_amenity['name'], "Wifi")

    def test_amenity_id_generator(self):
        amenity_test = Amenity()
        another_amenity_test = Amenity()
        self.assertEqual(amenity_test.id, another_amenity_test.id)

    def test_amenity_creation_instance(self):
        amenity_test = Amenity(name="Wifi")
        self.assertEqual(amenity_test.name, "Wifi")

    def test_amenity_inst_to_dict(self):
        amenity_test = Amenity(name="Wifi")
        dic_amenity = amenity_test.to_dict()
        self.assertEqual(dic_amenity['name'], "Wifi")

if __name__ == "__main__":
    unittest.main()
