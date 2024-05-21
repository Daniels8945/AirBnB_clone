#!/usr/bin/python3
"""Unittest module for the City Class"""

import os
import unittest
import models
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_city_attr(self):
        city_test = City()
        self.assertEqual(city_test.state_id, "")
        self.assertEqual(city_test.name, "")

    def test_city_inherits_from_basemodel(self):
        city_test = City()
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_str_rep(self):
        city_test = City()
        city_test.name = "New York"
        city_test.state_id = "NY"
        str_city = str(city_test)
        self.assertIn("City", str_city)
        self.assertIn("New York", str_city)
        self.assertIn("NY", str_city)

    def test_city_to_dict(self):
        city_test = City()
        city_test.name = "New York"
        city_test.state_id = "NY"
        city_test.save()
        dic_city = city_test.to_dict()
        self.assertEqual(dic_city['name'], "New York")
        self.assertEqual(dic_city['state_id'], "NY")

    def test_city_creation_instance(self):
        city_test = City(name="New York", state_id="NY")
        self.assertEqual(city_test.name, "New York")
        self.assertEqual(city_test.state_id, "NY")

    def test_city_inst_to_dict(self):
        city_test = City(name="New York", state_id="NY")
        dic_city = city_test.to_dict()
        self.assertEqual(dic_city['name'], "New York")
        self.assertEqual(dic_city['state_id'], "NY")

    def test_city_id_generator(self):
        city_test = City()
        another_city_test = City()
        self.assertEqual(city_test.id, another_city_test.id)


if __name__ == "__main__":
    unittest.main()
