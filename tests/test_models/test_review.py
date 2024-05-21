#!/usr/bin/python3
"""Unittest module for the Review Class"""

import os
import unittest
import models
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_review_attr(self):
        review_test = Review()
        self.assertEqual(review_test.place_id, "")
        self.assertEqual(review_test.user_id, "")
        self.assertEqual(review_test.text, "")

    def test_review_inherits_from_basemodel(self):
        review_test = Review()
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_str_rep(self):
        review_test = Review()
        review_test.text = "Great place to stay!"
        str_review = str(review_test)
        self.assertIn("Review", str_review)
        self.assertIn("Great place to stay!", str_review)

    def test_review_to_dict(self):
        review_test = Review()
        review_test.text = "Great place to stay!"
        review_test.save()
        dic_review = review_test.to_dict()
        self.assertEqual(dic_review['text'], "Great place to stay!")

    def test_review_creation_instance(self):
        review_test = Review(text="Great place to stay!")
        self.assertEqual(review_test.text, "Great place to stay!")

    def test_review_inst_to_dict(self):
        review_test = Review(text="Great place to stay!")
        dic_review = review_test.to_dict()
        self.assertEqual(dic_review['text'], "Great place to stay!")

    def test_review_id_generator(self):
        review_test = Review()
        another_review_test = Review()
        self.assertEqual(review_test.id, another_review_test.id)


if __name__ == "__main__":
    unittest.main()
