#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """Unittests for testing the City class."""
    def test_instantiation(self):
        """instantiates BaseModel correctly"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_City_storage(self):
        """tests that the storage is correctly set"""
        city = City()
        self.assertIn(city, storage.all().values())

    def test_str_id(self):
        """tests that the id is a string"""
        city = City()
        self.assertIsInstance(city.id, str)

    def test_name(self):
        """tests that the name is a string"""
        city = City()
        self.assertIsInstance(city.name, str)

    def test_state_id(self):
        """tests that the state_id is a string"""
        city = City()
        self.assertIsInstance(city.state_id, str)

    def test_created_at(self):
        """tests that the created_at is a datetime"""
        city = City()
        self.assertIsInstance(city.created_at, datetime)

    def test_updated_at(self):
        city = City()
        self.assertIsInstance(city.updated_at, datetime)

    def test_id_unique(self):
        """tests that the id is unique"""
        city = City()
        city_2 = City()
        self.assertNotEqual(city.id, city_2.id)

    def test_created_at_updated_at(self):
        """tests that created_at and updated_at are not the same"""
        city = City()
        city_2 = City()
        self.assertNotEqual(city.created_at, city_2.created_at)
        self.assertNotEqual(city.updated_at, city_2.updated_at)

    def test_save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        city = City()
        created = city.created_at
        updated = city.save()
        self.assertNotEqual(created, updated)

    def test_to_dict_type(self):
        """test that the dictionary returned is in the correct format"""
        city = City()
        new_dict = city.to_dict()
        self.assertIsInstance(new_dict, dict)

    def test_to_dict_attrs(self):
        """test that the dictionary returned has the correct attributes"""
        city = City()
        self.assertIn('id', city.to_dict())
        self.assertIn('created_at', city.to_dict())
        self.assertIn('updated_at', city.to_dict())
        self.assertIn('__class__', city.to_dict())

    def test_new_attrs(self):
        """test that new attributes can be added to the dictionary"""
        city = City()
        city.name = "James"
        city.age = 21
        self.assertIn('name', city.to_dict())
        self.assertIn('age', city.to_dict())

    def test_str_attrs(self):
        """test that the string representation of the BaseModel is correct"""
        city = City()
        new_dict = city.to_dict()
        self.assertIsInstance(new_dict['id'], str)
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)

    def test_datetime_iso(self):
        """test that the string representation of the BaseModel is correct"""
        city = City()
        new_dict = city.to_dict()
        self.assertEqual(new_dict['created_at'], city.created_at.isoformat())
        self.assertEqual(new_dict['updated_at'], city.updated_at.isoformat())

    def test_to_dict_with_args(self):
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)

    def test_str(self):
        """tests that the string representation of the BaseModel is correct"""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))

    def test__dict__(self):
        """tests that the dictionary representation of the
        BaseModel is correct"""
        city = City()
        self.assertNotEqual(city.to_dict(), city.__dict__)


if __name__ == "__main__":
    unittest.main()
