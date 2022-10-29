#!/usr/bin/env pyhton3
import pep8
import unittest
import datetime
import models
from models import base_model
BaseModel = base_model.BaseModel
"""
Test case for `BaseMdoel` class
"""


class TestBaseModel(unittest.TestCase):
    """
    Test case for edge cases for `BaseModel` class inherit by
    all other sub class models
    """

    def setUp(self):
        """
        set up method for the test
        """
        self.user1 = BaseModel()
        self.date_time = datetime.datetime.now()

    def test_Pep8StyleGuide(self):
        """
        Test for pep8 style guide in files
        """
        pep8_style = pep8.StyleGuide(quite=True)
        result = pep8_style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (Warning)")

    def test_doc_module(self):
        self.assertTrue(len(BaseModel.__doc__) > 1)

    def test_init_method(self):
        """
        Test for creating new instance using
        keyword arguments
        """
        json_dict = self.user1.to_dict()
        new_user = BaseModel(**json_dict)
        for key, value in json_dict.items():
            if key != "__class__":
                self.assertTrue(hasattr(new_user, key))
        self.assertEqual(new_user.id, self.user1.id)
        self.assertEqual(new_user.created_at, self.user1.created_at)
        self.assertEqual(new_user.updated_at, self.user1.updated_at)

    def test_unique_id(self):
        """
        Test for unique id of the BaseModel instances
        """
        user2 = BaseModel()
        user3 = BaseModel()
        self.assertIsInstance(self.user1.id, str)
        self.assertNotEqual(self.user1.id, user2.id)
        self.assertNotEqual(user2.id, user3.id)
        self.assertNotEqual(self.user1.id, user3.id)

    def test_create_datetime(self):
        """
        Test for the correct date and time of the created_at
        attribute
        """
        self.assertNotEqual(self.date_time.microsecond,
                            self.user1.created_at.microsecond)
        self.assertEqual(self.date_time.second, self.user1.created_at.second)
        self.assertEqual(self.date_time.year, self.user1.created_at.year)
        self.assertEqual(self.date_time.month, self.user1.created_at.month)
        self.assertEqual(self.date_time.day, self.user1.created_at.day)
        self.assertEqual(self.date_time.hour, self.user1.created_at.hour)
        self.assertEqual(self.date_time.minute, self.user1.created_at.minute)

    def test_update_datetime(self):
        """
        Test for the correct date and time for the updated_at
        attribute value
        """
        self.assertEqual(self.date_time.year, self.user1.updated_at.year)
        self.assertEqual(self.date_time.month, self.user1.updated_at.month)
        self.assertEqual(self.date_time.day, self.user1.updated_at.day)
        self.assertEqual(self.date_time.hour, self.user1.updated_at.hour)
        self.assertEqual(self.date_time.minute, self.user1.updated_at.minute)
        self.assertEqual(self.date_time.second, self.user1.updated_at.second)
        self.assertNotEqual(self.date_time.microsecond,
                            self.user1.updated_at.microsecond)

        models.storage.save()
        self.assertEqual(self.date_time.year, self.user1.updated_at.year)
        self.assertEqual(self.date_time.month, self.user1.updated_at.month)
        self.assertEqual(self.date_time.day, self.user1.updated_at.day)
        self.assertEqual(self.date_time.hour, self.user1.updated_at.hour)
        self.assertEqual(self.date_time.minute, self.user1.updated_at.minute)
        self.assertEqual(self.date_time.second, self.user1.updated_at.second)
        self.assertNotEqual(self.date_time.microsecond,
                            self.user1.updated_at.microsecond)

    def test_string_rep(self):
        """
        Test for the string representation of the BaseModel
        class
        """
        self.assertEqual(self.user1.__str__(),
                         f"[BaseModel] ({self.user1.id}) \
{self.user1.__dict__}")

    def test_save_method(self):
        """
        Test for the save method of the BaseModel
        class
        """
        self.user1.save()
        date_time = datetime.datetime.now()
        self.assertEqual(self.user1.updated_at.year, date_time.year)
        self.assertEqual(self.user1.updated_at.month, date_time.month)
        self.assertEqual(self.user1.updated_at.day, date_time.day)
        self.assertEqual(self.user1.updated_at.hour, date_time.hour)
        self.assertEqual(self.user1.updated_at.minute, date_time.minute)
        self.assertAlmostEqual(self.user1.updated_at.second,
                               date_time.second, places=10)

    def test_to_dict(self):
        """
        Test the to_dict method for content of the BaseModel
        class
        """
        self.assertTrue("id" in self.user1.to_dict())
        self.assertTrue("updated_at" in self.user1.to_dict())
        self.assertTrue("created_at" in self.user1.to_dict())
        self.assertTrue("__class__" in self.user1.to_dict())
        self.assertTrue("BaseModel" in self.user1.to_dict().values())
        self.assertTrue(self.user1.created_at.isoformat() in
                        self.user1.to_dict().values())
        self.assertTrue(self.user1.updated_at.isoformat() in
                        self.user1.to_dict().values())

    def tearDown(self):
        """
        Tear down method
        """
        del self.user1
        del self.date_time
