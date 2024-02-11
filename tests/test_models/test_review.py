#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """Unittests for testing the Review class."""
    def test_instantiation(self):
        """instantiates BaseModel correctly"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_Review_storage(self):
        """tests that the storage is correctly set"""
        review = Review()
        self.assertIn(review, storage.all().values())

    def test_str_id(self):
        """tests that the id is a string"""
        review = Review()
        self.assertIsInstance(review.id, str)

    def test_place_id(self):
        """tests that the place_id is a string"""
        review = Review()
        self.assertIsInstance(review.place_id, str)

    def test_user_id(self):
        """tests that the user_id is a string"""
        review = Review()
        self.assertIsInstance(review.user_id, str)

    def test_text(self):
        """tests that the text is a string"""
        review = Review()
        self.assertIsInstance(review.text, str)

    def test_created_at(self):
        """tests that the created_at is a datetime"""
        review = Review()
        self.assertIsInstance(review.created_at, datetime)

    def test_updated_at(self):
        review = Review()
        self.assertIsInstance(review.updated_at, datetime)

    def test_id_unique(self):
        """tests that the id is unique"""
        review = Review()
        review_2 = Review()
        self.assertNotEqual(review.id, review_2.id)

    def test_created_at_updated_at(self):
        """tests that created_at and updated_at are not the same"""
        review = Review()
        review_2 = Review()
        self.assertNotEqual(review.created_at, review_2.created_at)
        self.assertNotEqual(review.updated_at, review_2.updated_at)

    def test_save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        review = Review()
        created = review.created_at
        updated = review.save()
        self.assertNotEqual(created, updated)

    def test_to_dict_type(self):
        """test that the dictionary returned is in the correct format"""
        review = Review()
        new_dict = review.to_dict()
        self.assertIsInstance(new_dict, dict)

    def test_to_dict_attrs(self):
        """test that the dictionary returned has the correct attributes"""
        review = Review()
        self.assertIn('id', review.to_dict())
        self.assertIn('created_at', review.to_dict())
        self.assertIn('updated_at', review.to_dict())
        self.assertIn('__class__', review.to_dict())

    def test_new_attrs(self):
        """test that new attributes can be added to the dictionary"""
        review = Review()
        review.name = "James"
        review.age = 21
        self.assertIn('name', review.to_dict())
        self.assertIn('age', review.to_dict())

    def test_str_attrs(self):
        """test that the string representation of the BaseModel is correct"""
        review = Review()
        new_dict = review.to_dict()
        self.assertIsInstance(new_dict['id'], str)
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)

    def test_datetime_iso(self):
        """test that the string representation of the BaseModel is correct"""
        review = Review()
        new_dict = review.to_dict()
        self.assertEqual(new_dict['created_at'], review.created_at.isoformat())
        self.assertEqual(new_dict['updated_at'], review.updated_at.isoformat())

    def test_to_dict_with_args(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.to_dict(None)

    def test_str(self):
        """tests that the string representation of the BaseModel is correct"""
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))

    def test__dict__(self):
        """tests that the dictionary representation of the
        BaseModel is correct"""
        review = Review()
        self.assertNotEqual(review.to_dict(), review.__dict__)


if __name__ == "__main__":
    unittest.main()
