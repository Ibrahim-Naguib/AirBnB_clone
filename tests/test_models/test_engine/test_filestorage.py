#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
  """Unittests for testing the FileStorage class."""

  def test_FileStorage_instantiation(self):
    storage = FileStorage()
    self.assertIsInstance(storage, FileStorage)

  def test_instantiation_with_args(self):
    with self.assertRaises(TypeError):
        FileStorage(None)

  def test_FileStorage_path(self):
    storage = FileStorage()
    self.assertEqual(str, type(storage._FileStorage__file_path))

  def test_FileStorage_objects(self):
    storage = FileStorage()
    self.assertEqual(dict, type(storage._FileStorage__objects))

  def test_initalized(self):
    storage = FileStorage()
    self.assertEqual(type(storage), FileStorage)
    
  def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

  def tearDown(self):
      try:
          os.remove("file.json")
      except IOError:
          pass
      try:
          os.rename("tmp", "file.json")
      except IOError:
          pass
      FileStorage._FileStorage__objects = {}

  def test_FileStorage_all(self):
    """Tests all method of FileStorage class."""
    storage = FileStorage()
    self.assertIsInstance(storage.all(), dict)

  def test_all_with_args(self):
    with self.assertRaises(TypeError):
        storage = FileStorage()
        storage.all(None)

  def test_new(self):
    """Tests new method of FileStorage class."""
    storage = FileStorage()
    base_model = BaseModel()
    user = User()
    city = City()
    state = State()
    amenity = Amenity()
    place = Place()
    review = Review()

    storage.new(base_model)
    storage.new(user)
    storage.new(city)
    storage.new(state)
    storage.new(amenity)
    storage.new(place)
    storage.new(review)

    self.assertIn(base_model, storage.all().values())
    self.assertIn(user, storage.all().values())
    self.assertIn(city, storage.all().values())
    self.assertIn(state, storage.all().values())
    self.assertIn(amenity, storage.all().values())
    self.assertIn(place, storage.all().values())
    self.assertIn(review, storage.all().values())

    self.assertIn("BaseModel." + base_model.id, storage.all().keys())
    self.assertIn("User." + user.id, storage.all().keys())
    self.assertIn("City." + city.id, storage.all().keys())
    self.assertIn("State." + state.id, storage.all().keys())
    self.assertIn("Amenity." + amenity.id, storage.all().keys())
    self.assertIn("Place." + place.id, storage.all().keys())
    self.assertIn("Review." + review.id, storage.all().keys())

  def test_new_with_args(self):
    with self.assertRaises(TypeError):
        storage = FileStorage()
        storage.new(User, None)
    
  def test_save(self):
    """Tests save method of FileStorage class."""
    storage = FileStorage()
    base_model = BaseModel()
    user = User()
    city = City()
    state = State()
    amenity = Amenity()
    place = Place()
    review = Review()

    storage.new(base_model)
    storage.new(user)
    storage.new(city)
    storage.new(state)
    storage.new(amenity)
    storage.new(place)
    storage.new(review)
    storage.save()
    text = ""
    with open("file.json", "r") as f:
        text = f.read()
    self.assertIn("BaseModel." + base_model.id, text)
    self.assertIn("User." + user.id, text)
    self.assertIn("City." + city.id, text)
    self.assertIn("State." + state.id, text)
    self.assertIn("Amenity." + amenity.id, text)
    self.assertIn("Place." + place.id, text)
    self.assertIn("Review." + review.id, text)
    
  def test_save_with_args(self):
    with self.assertRaises(TypeError):
        storage = FileStorage()
        storage.save(None)

  def test_reload(self):
    """Tests reload method of FileStorage class."""
    storage = FileStorage()
    base_model = BaseModel()
    user = User()
    city = City()
    state = State()
    amenity = Amenity()
    place = Place()
    review = Review()

    storage.new(base_model)
    storage.new(user)
    storage.new(city)
    storage.new(state)
    storage.new(amenity)
    storage.new(place)
    storage.new(review)
    storage.save()
    storage.reload()
    objects = FileStorage._FileStorage__objects
    self.assertIn("BaseModel." + base_model.id, objects)
    self.assertIn("User." + user.id, objects)
    self.assertIn("City." + city.id, objects)
    self.assertIn("State." + state.id, objects)
    self.assertIn("Amenity." + amenity.id, objects)
    self.assertIn("Place." + place.id, objects)
    self.assertIn("Review." + review.id, objects)

  def test_reload_with_args(self):
      with self.assertRaises(TypeError):
          storage = FileStorage()
          storage.reload(None)

if __name__ == "__main__":
    unittest.main()