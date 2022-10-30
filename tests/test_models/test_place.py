#!/usr/bin/env python3
import unittest
import pep8
from models.place import Place
"""
Test for Place model class
"""


class TestPlaceClass(unittest.TestCase):
    """
    Tet class Place
    """

    def setUp(self):
        """
        setup class instance
        """
        self.place = Place()

    def test_pep8_style_guide(self):
        """
        Test  pep8 style guide for the file
        """
        pep8_style = pep8.StyleGuide(quite=True)
        result = pep8_style.check_files(["models/place.py"])
        self.assertEqual(result.total_errors, 0)

    def test_for_attr(self):
        """
        Test class for attribute
        """
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "state_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))

    def test_str_rep(self):
        """
        Test for string representation of user object
        """
        self.assertEqual(self.place.__str__(),
                         "[Place] ({}) {}".format(self.place.id,
                                                 self.place.__dict__))

    def tearDown(self):
        """
        tear down place instance
        """
        del self.place
