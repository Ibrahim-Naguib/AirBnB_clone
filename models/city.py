#!/usr/bin/python3
"""This module defines a class City"""

from models.base_model import BaseModel


class City(BaseModel):
  """This class defines a city"""
  state_id = ""
  name = ""