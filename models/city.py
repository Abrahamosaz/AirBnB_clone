#!/usr/bin/env python3
from models.base_model import BaseModel
"""
city model that inherit from BaseModel
"""


class City(BaseModel):
    """
    City model with public class attribute `state_id` and `name`
    """
    state_id = ""
    name = ""
