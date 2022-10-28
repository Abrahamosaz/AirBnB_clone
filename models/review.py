#!/usr/bin/env python3
from models.base_model import BaseModel
"""
review model that inherit from BaseModel
"""


class Review(BaseModel):
    """
    review models
    """
    place_id = ""
    user_id = ""
    text = ""
