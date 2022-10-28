#!/usr/bin/env python3
from .engine.file_storage import FileStorage
from . import base_model, user, place, review, amenity, state
"""
instantiate filestorage instance
"""
storage = FileStorage()
storage.reload()
