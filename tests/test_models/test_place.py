#!/usr/bin/python3
"""Unittest module for the Place Class"""

import os
import unittest
import models
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_place_attr(self):
        place_test = Place()
        self.assertEqual(place_test.city_id, "")
        self.assertEqual(place_test.user_id, "")
        self.assertEqual(place_test.name, "")
        self.assertEqual(place_test.description, "")
        self.assertEqual(place_test.number_rooms, 0)
        self.assertEqual(place_test.number_bathrooms, 0)
        self.assertEqual(place_test.max_guest, 0)
        self.assertEqual(place_test.price_by_night, 0)
        self.assertEqual(place_test.latitude, 0.0)
        self.assertEqual(place_test.longitude, 0.0)
        self.assertEqual(place_test.amenity_ids, [])

    def test_place_inherits_from_basemodel(self):
        place_test = Place()
        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_str_rep(self):
        place_test = Place()
        place_test.name = "Cozy Apartment"
        str_place = str(place_test)
        self.assertIn("Place", str_place)
        self.assertIn("Cozy Apartment", str_place)

    def test_place_to_dict(self):
        place_test = Place()
        place_test.name = "Cozy Apartment"
        place_test.save()
        dic_place = place_test.to_dict()
        self.assertEqual(dic_place['name'], "Cozy Apartment")

    def test_place_creation_instance(self):
        place_test = Place(name="Cozy Apartment")
        self.assertEqual(place_test.name, "Cozy Apartment")

    def test_place_inst_to_dict(self):
        place_test = Place(name="Cozy Apartment")
        dic_place = place_test.to_dict()
        self.assertEqual(dic_place['name'], "Cozy Apartment")

    def test_place_id_generator(self):
        place_test = Place()
        another_place_test = Place()
        self.assertEqual(place_test.id, another_place_test.id)


if __name__ == "__main__":
    unittest.main()
