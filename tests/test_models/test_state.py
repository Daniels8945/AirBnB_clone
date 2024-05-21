#!/usr/bin/python3
"""Unittest module for the State Class"""

import os
import unittest
import models
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_state_attr(self):
        state_test = State()
        self.assertEqual(state_test.name, "")

    def test_state_inherits_from_basemodel(self):
        state_test = State()
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_str_rep(self):
        state_test = State()
        state_test.name = "California"
        str_state = str(state_test)
        self.assertIn("State", str_state)
        self.assertIn("California", str_state)

    def test_state_to_dict(self):
        state_test = State()
        state_test.name = "California"
        state_test.save()
        dic_state = state_test.to_dict()
        self.assertEqual(dic_state['name'], "California")

    def test_state_creation_instance(self):
        state_test = State(name="California")
        self.assertEqual(state_test.name, "California")

    def test_state_inst_to_dict(self):
        state_test = State(name="California")
        dic_state = state_test.to_dict()
        self.assertEqual(dic_state['name'], "California")

    def test_state_id_generator(self):
        state_test = State()
        another_state_test = State()
        self.assertEqual(state_test.id, another_state_test.id)


if __name__ == "__main__":
    unittest.main()
