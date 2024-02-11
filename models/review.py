#!/usr/bin/python3
"""This module defines a class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
  """This class inherits from BaseModel"""
  place_id = ""
  user_id = ""
  text = ""