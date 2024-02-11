#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unittests for testing the Place class."""
    def test_instantiation(self):
        """instantiates BaseModel correctly"""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_Place_storage(self):
        """tests that the storage is correctly set"""
        place = Place()
        self.assertIn(place, storage.all().values())

    def test_str_id(self):
        """tests that the id is a string"""
        place = Place()
        self.assertIsInstance(place.id, str)

    def test_city_id(self):
        """tests that the city_id is a string"""
        place = Place()
        self.assertIsInstance(place.city_id, str)

    def test_user_id(self):
        """tests that the user_id is a string"""
        place = Place()
        self.assertIsInstance(place.user_id, str)

    def test_name(self):
        """tests that the name is a string"""
        place = Place()
        self.assertIsInstance(place.name, str)

    def test_description(self):
        """tests that the description is a string"""
        place = Place()
        self.assertIsInstance(place.description, str)

    def test_number_rooms(self):
        """tests that the number_rooms is an integer"""
        place = Place()
        self.assertIsInstance(place.number_rooms, int)

    def test_number_bathrooms(self):
        """tests that the number_bathrooms is an integer"""
        place = Place()
        self.assertIsInstance(place.number_bathrooms, int)

    def test_max_guest(self):
        """tests that the max_guest is an integer"""
        place = Place()
        self.assertIsInstance(place.max_guest, int)

    def test_price_by_night(self):
        """tests that the price_by_night is an integer"""
        place = Place()
        self.assertIsInstance(place.price_by_night, int)

    def test_latitude(self):
        """tests that the latitude is a float"""
        place = Place()
        self.assertIsInstance(place.latitude, float)

    def test_longitude(self):
        """tests that the longitude is a float"""
        place = Place()
        self.assertIsInstance(place.longitude, float)

    def test_amenity_ids(self):
        """tests that the amenity_ids is a list"""
        place = Place()
        self.assertIsInstance(place.amenity_ids, list)

    def test_created_at(self):
        """tests that the created_at is a datetime"""
        place = Place()
        self.assertIsInstance(place.created_at, datetime)

    def test_updated_at(self):
        place = Place()
        self.assertIsInstance(place.updated_at, datetime)

    def test_id_unique(self):
        """tests that the id is unique"""
        place = Place()
        place_2 = Place()
        self.assertNotEqual(place.id, place_2.id)

    def test_created_at_updated_at(self):
        """tests that created_at and updated_at are not the same"""
        place = Place()
        place_2 = Place()
        self.assertNotEqual(place.created_at, place_2.created_at)
        self.assertNotEqual(place.updated_at, place_2.updated_at)

    def test_save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        place = Place()
        created = place.created_at
        updated = place.save()
        self.assertNotEqual(created, updated)

    def test_to_dict_type(self):
        """test that the dictionary returned is in the correct format"""
        place = Place()
        new_dict = place.to_dict()
        self.assertIsInstance(new_dict, dict)

    def test_to_dict_attrs(self):
        """test that the dictionary returned has the correct attributes"""
        place = Place()
        self.assertIn('id', place.to_dict())
        self.assertIn('created_at', place.to_dict())
        self.assertIn('updated_at', place.to_dict())
        self.assertIn('__class__', place.to_dict())

    def test_new_attrs(self):
        """test that new attributes can be added to the dictionary"""
        place = Place()
        place.name = "James"
        place.age = 21
        self.assertIn('name', place.to_dict())
        self.assertIn('age', place.to_dict())

    def test_str_attrs(self):
        """test that the string representation of the BaseModel is correct"""
        place = Place()
        new_dict = place.to_dict()
        self.assertIsInstance(new_dict['id'], str)
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)

    def test_datetime_iso(self):
        """test that the string representation of the BaseModel is correct"""
        place = Place()
        new_dict = place.to_dict()
        self.assertEqual(new_dict['created_at'], place.created_at.isoformat())
        self.assertEqual(new_dict['updated_at'], place.updated_at.isoformat())

    def test_to_dict_with_args(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.to_dict(None)

    def test_str(self):
        """tests that the string representation of the BaseModel is correct"""
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))

    def test__dict__(self):
        """tests that the dictionary representation of the
        BaseModel is correct"""
        place = Place()
        self.assertNotEqual(place.to_dict(), place.__dict__)


if __name__ == "__main__":
    unittest.main()
