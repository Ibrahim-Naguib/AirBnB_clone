#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
  """Unittests for testing the State class."""

  def test_instantiation(self):
    """instantiates BaseModel correctly"""
    state = State()
    self.assertIsInstance(state, BaseModel)

  def test_State_storage(self):
    """tests that the storage is correctly set"""
    state = State()
    self.assertIn(state, storage.all().values())

  def test_str_id(self):
    """tests that the id is a string"""
    state = State()
    self.assertIsInstance(state.id, str)

  def test_name(self):
    """tests that the name is a string"""
    state = State()
    self.assertIsInstance(state.name, str)
    
  def test_created_at(self):
    """tests that the created_at is a datetime"""
    state = State()
    self.assertIsInstance(state.created_at, datetime)

  def test_updated_at(self):
    state = State()
    self.assertIsInstance(state.updated_at, datetime)

  def test_id_unique(self):
    """tests that the id is unique"""
    state = State()
    state_2 = State()
    self.assertNotEqual(state.id, state_2.id)

  def test_created_at_updated_at(self):
    """tests that created_at and updated_at are not the same"""
    state = State()
    state_2 = State()
    self.assertNotEqual(state.created_at, state_2.created_at)
    self.assertNotEqual(state.updated_at, state_2.updated_at)

  def test_save(self):
    """updates the public instance attribute updated_at
    with the current datetime"""
    state = State()
    created = state.created_at
    updated = state.save()
    self.assertNotEqual(created, updated)

  def test_to_dict_type(self):
    """test that the dictionary returned is in the correct format"""
    state = State()
    new_dict = state.to_dict()
    self.assertIsInstance(new_dict, dict)
  
  def test_to_dict_attrs(self):
    """test that the dictionary returned has the correct attributes"""
    state = State()
    self.assertIn('id', state.to_dict())
    self.assertIn('created_at', state.to_dict())
    self.assertIn('updated_at', state.to_dict())
    self.assertIn('__class__', state.to_dict())

  def test_new_attrs(self):
    """test that new attributes can be added to the dictionary"""
    state = State()
    state.name = "James"
    state.age = 21
    self.assertIn('name', state.to_dict())
    self.assertIn('age', state.to_dict())

  def test_str_attrs(self):
    """test that the string representation of the BaseModel is correct"""
    state = State()
    new_dict = state.to_dict()
    self.assertIsInstance(new_dict['id'], str)
    self.assertIsInstance(new_dict['created_at'], str)
    self.assertIsInstance(new_dict['updated_at'], str)

  def test_datetime_iso(self):
    """test that the string representation of the BaseModel is correct"""
    state = State()
    new_dict = state.to_dict()
    self.assertEqual(new_dict['created_at'], state.created_at.isoformat())
    self.assertEqual(new_dict['updated_at'], state.updated_at.isoformat())

  def test_to_dict_with_args(self):
    state = State()
    with self.assertRaises(TypeError):
      state.to_dict(None)

  def test_str(self):
    """tests that the string representation of the BaseModel is correct"""
    state = State()
    string = "[State] ({}) {}".format(state.id, state.__dict__)
    self.assertEqual(string, str(state))

  def test__dict__(self):
    """tests that the dictionary representation of the BaseModel is correct"""
    state = State()
    self.assertNotEqual(state.to_dict(), state.__dict__)

  if __name__ == "__main__":
    unittest.main()