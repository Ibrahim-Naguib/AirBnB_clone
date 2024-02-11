"""This module defines the package models"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
