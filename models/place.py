#!/usr/bin/env python3
from models.base_model import BaseModel
"""
Place models inherit from BaseModel
"""


class Place(BaseModel):
    """
    Place model with many public attribute
    that describe a place
    """
    city_id = ""
    state_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
