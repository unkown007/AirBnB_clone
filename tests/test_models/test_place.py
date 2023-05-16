#!/usr/bin/python3
""" unittest for the amenity class """


import unittest
from models.place import Place
import os


class TestPlace(unittest.TestCase):
    """ Test Cases """

    @classmethod
    def setUpClass(cls):
        """ Getting everything ready """
        cls.ins = Place()

    @classmethod
    def teardown(cls):
        """ cleaning up everything """
        del cls.ins
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_BaseModelAttr(self):
        """ testing base model attributes """
        self.assertEqual(hasattr(self.ins, "city_id"), True)
        self.assertEqual(hasattr(self.ins, "user_id"), True)
        self.assertEqual(hasattr(self.ins, "name"), True)
        self.assertEqual(hasattr(self.ins, "description"), True)
        self.assertEqual(hasattr(self.ins, "number_rooms"), True)
        self.assertEqual(hasattr(self.ins, "number_bathrooms"), True)
        self.assertEqual(hasattr(self.ins, "max_guest"), True)
        self.assertEqual(hasattr(self.ins, "price_by_night"), True)
        self.assertEqual(hasattr(self.ins, "latitude"), True)
        self.assertEqual(hasattr(self.ins, "longitude"), True)
        self.assertEqual(hasattr(self.ins, "amenity_ids"), True)

    def test_isinstance(self):
        """ testing the instance """
        self.assertTrue(isinstance(self.ins, Place))

if __name__ == '__main__':
    unittest.main()
