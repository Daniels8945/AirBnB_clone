#!/usr/bin/python3
"""Unittest module for the User Class"""

import os
import unittest
import models
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_attr(self):
        user_test = User()
        self.assertEqual(user_test.email, "")
        self.assertEqual(user_test.password, "")
        self.assertEqual(user_test.first_name, "")
        self.assertEqual(user_test.last_name, "")

    def test_user_inherits_from_basemodel(self):
        user_test = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str_rep(self):
        user_test = User()
        user_test.email = "ourtest@example.com"
        user_test.first_name = "ourtest"
        user_test.last_name = "danial"
        user_test.password = "pass_123@"
        str_user = str(user_test)
        self.assertIn("User", str_user)
        self.assertIn("ourtest@example.com", str_user)
        self.assertIn("ourtest", str_user)
        self.assertIn("danial", str_user)

    def test_user_to_dict(self):
        user_test = User()
        user_test.email = "ourtest@example.com"
        user_test.first_name = "ourtest"
        user_test.last_name = "danial"
        user_test.save()
        dic_user = user_test.to_dict()
        self.assertEqual(dic_user['email'], "ourtest@example.com")
        self.assertEqual(dic_user['first_name'], "ourtest")
        self.assertEqual(dic_user['last_name'], "danial")

    def test_user_creation_instance(self):
        user_test = User(email="ourtest@example.com", password="pass_123@",
                    first_name="ourtest", last_name="danial")
        self.assertEqual(user_test.email, "ourtest@example.com")
        self.assertEqual(user_test.password, "pass_123@")
        self.assertEqual(user_test.first_name, "ourtest")
        self.assertEqual(user_test.last_name, "danial")

    def test_user_inst_to_dict(self):
        user_test = User(email="ourtest@example.com", password="pass_123@",
                    first_name="ourtest", last_name="danial")
        dic_user = user_test.to_dict()
        self.assertEqual(dic_user['email'], "ourtest@example.com")
        self.assertEqual(dic_user['password'], "pass_123@")
        self.assertEqual(dic_user['first_name'], "ourtest")
        self.assertEqual(dic_user['last_name'], "danial")

    def test_user_id_generator(self):
        user_test = User()
        another_user_test = User()
        self.assertEqual(user_test.id, another_user_test.id)


if __name__ == "__main__":
    unittest.main()
