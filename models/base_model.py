#!/usr/bin/python3
"""Defines a class BaseModel"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel

        Args:
            *args (any): Unused.
            **kwargs (any): key/value pairs of attributes.
        """
        TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, TIME_FORMAT)
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def save(self):
        """updates the updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dict containing all keys/values of the instanc"""
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """returns a string representation of the BaseModel class"""
        cls = self.__class__.__name__
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)
