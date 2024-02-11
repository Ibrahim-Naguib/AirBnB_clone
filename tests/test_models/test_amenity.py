#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for testing the Amenity class."""
    def test_instantiation(self):
        """instantiates BaseModel correctly"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_Amenity_storage(self):
        """tests that the storage is correctly set"""
        amenity = Amenity()
        self.assertIn(amenity, storage.all().values())

    def test_str_id(self):
        """tests that the id is a string"""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)

    def test_name(self):
        """tests that the name is a string"""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_created_at(self):
        """tests that the created_at is a datetime"""
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime)

    def test_updated_at(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_id_unique(self):
        """tests that the id is unique"""
        amenity = Amenity()
        amenity_2 = Amenity()
        self.assertNotEqual(amenity.id, amenity_2.id)

    def test_created_at_updated_at(self):
        """tests that created_at and updated_at are not the same"""
        amenity = Amenity()
        amenity_2 = Amenity()
        self.assertNotEqual(amenity.created_at, amenity_2.created_at)
        self.assertNotEqual(amenity.updated_at, amenity_2.updated_at)

    def test_save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        amenity = Amenity()
        created = amenity.created_at
        updated = amenity.save()
        self.assertNotEqual(created, updated)

    def test_to_dict_type(self):
        """test that the dictionary returned is in the correct format"""
        amenity = Amenity()
        new_dict = amenity.to_dict()
        self.assertIsInstance(new_dict, dict)

    def test_to_dict_attrs(self):
        """test that the dictionary returned has the correct attributes"""
        amenity = Amenity()
        self.assertIn('id', amenity.to_dict())
        self.assertIn('created_at', amenity.to_dict())
        self.assertIn('updated_at', amenity.to_dict())
        self.assertIn('__class__', amenity.to_dict())

    def test_new_attrs(self):
        """test that new attributes can be added to the dictionary"""
        amenity = Amenity()
        amenity.name = "James"
        amenity.age = 21
        self.assertIn('name', amenity.to_dict())
        self.assertIn('age', amenity.to_dict())

    def test_str_attrs(self):
        """test that the string representation of the BaseModel is correct"""
        amenity = Amenity()
        new_dict = amenity.to_dict()
        self.assertIsInstance(new_dict['id'], str)
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)

    def test_datetime_iso(self):
        """test that the string representation of the BaseModel is correct"""
        amenity = Amenity()
        new_dict = amenity.to_dict()
        self.assertEqual(new_dict['created_at'],
                         amenity.created_at.isoformat())
        self.assertEqual(new_dict['updated_at'],
                         amenity.updated_at.isoformat())

    def test_to_dict_with_args(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.to_dict(None)

    def test_str(self):
        """tests that the string representation of the BaseModel is correct"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))

    def test__dict__(self):
        """tests that the dictionary representation of the
        BaseModel is correct"""
        amenity = Amenity()
        self.assertNotEqual(amenity.to_dict(), amenity.__dict__)


if __name__ == "__main__":
    unittest.main()
