#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
  """Unittests for testing the BaseModel class."""

  def test_instantiation(self):
    """instantiates BaseModel correctly"""
    base_model = BaseModel()
    self.assertIsInstance(base_model, BaseModel)

  def test_basemodel_storage(self):
    """tests that the storage is correctly set"""
    base_model = BaseModel()
    self.assertIn(base_model, storage.all().values())

  def test_str_id(self):
    """tests that the id is a string"""
    base_model = BaseModel()
    self.assertIsInstance(base_model.id, str)

  def test_created_at(self):
    """tests that the created_at is a datetime"""
    base_model = BaseModel()
    self.assertIsInstance(base_model.created_at, datetime)

  def test_updated_at(self):
    base_model = BaseModel()
    self.assertIsInstance(base_model.updated_at, datetime)

  def test_id_unique(self):
    """tests that the id is unique"""
    base_model = BaseModel()
    base_model_2 = BaseModel()
    self.assertNotEqual(base_model.id, base_model_2.id)

  def test_created_at_updated_at(self):
    """tests that created_at and updated_at are not the same"""
    base_model = BaseModel()
    base_model_2 = BaseModel()
    self.assertNotEqual(base_model.created_at, base_model_2.created_at)
    self.assertNotEqual(base_model.updated_at, base_model_2.updated_at)

  def test_save(self):
    """updates the public instance attribute updated_at
    with the current datetime"""
    base_model = BaseModel()
    created = base_model.created_at
    updated = base_model.save()
    self.assertNotEqual(created, updated)

  def test_to_dict_type(self):
    """test that the dictionary returned is in the correct format"""
    base_model = BaseModel()
    new_dict = base_model.to_dict()
    self.assertIsInstance(new_dict, dict)
  
  def test_to_dict_attrs(self):
    """test that the dictionary returned has the correct attributes"""
    base_model = BaseModel()
    self.assertIn('id', base_model.to_dict())
    self.assertIn('created_at', base_model.to_dict())
    self.assertIn('updated_at', base_model.to_dict())
    self.assertIn('__class__', base_model.to_dict())

  def test_new_attrs(self):
    """test that new attributes can be added to the dictionary"""
    base_model = BaseModel()
    base_model.name = "James"
    base_model.age = 21
    self.assertIn('name', base_model.to_dict())
    self.assertIn('age', base_model.to_dict())

  def test_str_attrs(self):
    """test that the string representation of the BaseModel is correct"""
    base_model = BaseModel()
    new_dict = base_model.to_dict()
    self.assertIsInstance(new_dict['id'], str)
    self.assertIsInstance(new_dict['created_at'], str)
    self.assertIsInstance(new_dict['updated_at'], str)

  def test_datetime_iso(self):
    """test that the string representation of the BaseModel is correct"""
    base_model = BaseModel()
    new_dict = base_model.to_dict()
    self.assertEqual(new_dict['created_at'], base_model.created_at.isoformat())
    self.assertEqual(new_dict['updated_at'], base_model.updated_at.isoformat())

  def test_to_dict_with_args(self):
    base_model = BaseModel()
    with self.assertRaises(TypeError):
      base_model.to_dict(None)

  def test_str(self):
    """tests that the string representation of the BaseModel is correct"""
    base_model = BaseModel()
    string = "[BaseModel] ({}) {}".format(base_model.id, base_model.__dict__)
    self.assertEqual(string, str(base_model))

  def test__dict__(self):
    """tests that the dictionary representation of the BaseModel is correct"""
    base_model = BaseModel()
    self.assertNotEqual(base_model.to_dict(), base_model.__dict__)

  if __name__ == "__main__":
    unittest.main()