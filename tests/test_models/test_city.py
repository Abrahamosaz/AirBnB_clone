#!/usr/bin/env pytihon3
from models.city import City
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
        self.city = City()

    def test_pep8_style_guide(self):
        """
        Test for pep8 style guide in the file
        """
        pep8_style = pep8.StyleGuide(quite=True)
        result = pep8_style.check_files(["models/city.py"])
        self.assertEqual(result.total_errors, 0)

    def test_class_attr(self):
        """
        Test the class atrriute
        """
        self.assertTrue(hasattr(City, "state_id"))
        self.assertTrue(hasattr(City, "name"))
    
    def test_str_rep(self):
        """
        Test for string representation of user object
        """
        self.assertEqual(self.city.__str__(),
                         "[City] ({}) {}".format(self.city.id,
                                                 self.city.__dict__))

    def test_for_inheritedMethod(self):
        """
        Test for method inherited from the super class
        """
        city_attr = dir(City)
        self.assertTrue("save" in city_attr)
        self.assertTrue("to_dict" in city_attr)
