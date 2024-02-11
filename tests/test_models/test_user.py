#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """Unittests for testing the User class."""
    def test_instantiation(self):
        """instantiates BaseModel correctly"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_User_storage(self):
        """tests that the storage is correctly set"""
        user = User()
        self.assertIn(user, storage.all().values())

    def test_str_id(self):
        """tests that the id is a string"""
        user = User()
        self.assertIsInstance(user.id, str)

    def test_email(self):
        """tests that the email is a string"""
        user = User()
        self.assertIsInstance(user.email, str)

    def test_password(self):
        """tests that the password is a string"""
        user = User()
        self.assertIsInstance(user.password, str)

    def test_first_name(self):
        """tests that the first_name is a string"""
        user = User()
        self.assertIsInstance(user.first_name, str)

    def test_last_name(self):
        """tests that the last_name is a string"""
        user = User()
        self.assertIsInstance(user.last_name, str)

    def test_created_at(self):
        """tests that the created_at is a datetime"""
        user = User()
        self.assertIsInstance(user.created_at, datetime)

    def test_updated_at(self):
        user = User()
        self.assertIsInstance(user.updated_at, datetime)

    def test_id_unique(self):
        """tests that the id is unique"""
        user = User()
        user_2 = User()
        self.assertNotEqual(user.id, user_2.id)

    def test_created_at_updated_at(self):
        """tests that created_at and updated_at are not the same"""
        user = User()
        user_2 = User()
        self.assertNotEqual(user.created_at, user_2.created_at)
        self.assertNotEqual(user.updated_at, user_2.updated_at)

    def test_save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        user = User()
        created = user.created_at
        updated = user.save()
        self.assertNotEqual(created, updated)

    def test_to_dict_type(self):
        """test that the dictionary returned is in the correct format"""
        user = User()
        new_dict = user.to_dict()
        self.assertIsInstance(new_dict, dict)

    def test_to_dict_attrs(self):
        """test that the dictionary returned has the correct attributes"""
        user = User()
        self.assertIn('id', user.to_dict())
        self.assertIn('created_at', user.to_dict())
        self.assertIn('updated_at', user.to_dict())
        self.assertIn('__class__', user.to_dict())

    def test_new_attrs(self):
        """test that new attributes can be added to the dictionary"""
        user = User()
        user.name = "James"
        user.age = 21
        self.assertIn('name', user.to_dict())
        self.assertIn('age', user.to_dict())

    def test_str_attrs(self):
        """test that the string representation of the BaseModel is correct"""
        user = User()
        new_dict = user.to_dict()
        self.assertIsInstance(new_dict['id'], str)
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)

    def test_datetime_iso(self):
        """test that the string representation of the BaseModel is correct"""
        user = User()
        new_dict = user.to_dict()
        self.assertEqual(new_dict['created_at'], user.created_at.isoformat())
        self.assertEqual(new_dict['updated_at'], user.updated_at.isoformat())

    def test_to_dict_with_args(self):
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)

    def test_str(self):
        """tests that the string representation of the BaseModel is correct"""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))

    def test__dict__(self):
        """tests that the dictionary representation of the
        BaseModel is correct"""
        user = User()
        self.assertNotEqual(user.to_dict(), user.__dict__)


if __name__ == "__main__":
    unittest.main()
