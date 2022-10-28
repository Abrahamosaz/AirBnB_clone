#!/usr/bin/env python3
from models.base_model import BaseModel
"""
user Models inherit from BaseModel class
"""


class User(BaseModel):
    """
    User class that define the attribute of a user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
