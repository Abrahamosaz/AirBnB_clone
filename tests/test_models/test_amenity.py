#!/usr/bin/env pytihon3
from models.amenity import Amenity
import unittest
import pep8
"""
Test the user class
"""


class TestUserClass(unittest.TestCase):
    """
    Test for user class models in the dtabase file
    storage engine
    """

    def setUp(self):
        """
        setup the user class instance for test cases
        """
        self.amenity = Amenity()

    def test_pep8_style_guide(self):
        """
        Test for pep8 style guide in the file
        """
        pep8_style = pep8.StyleGuide(quite=True)
        result = pep8_style.check_files(["models/amenity.py"])
        self.assertEqual(result.total_errors, 0)

    def test_class_attr(self):
        """
        Test the class atrriute
        """
        self.assertTrue(hasattr(Amenity, "name"))
    
    def test_str_rep(self):
        """
        Test for string representation of user object
        """
        self.assertEqual(self.amenity.__str__(),
                         "[Amenity] ({}) {}".format(self.amenity.id,
                                                 self.amenity.__dict__))

    def test_for_inheritedMethod(self):
        """
        Test for methof inherited from the super class
        """
        amenity_attr = dir(Amenity)
        self.assertTrue("save" in amenity_attr)
        self.assertTrue("to_dict" in amenity_attr)
