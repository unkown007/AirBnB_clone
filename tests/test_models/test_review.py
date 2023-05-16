#!/usr/bin/python3
""" unittest for the amenity class """


import unittest
from models.review import Review
import os


class TestAmenity(unittest.TestCase):
    """ Test Cases """

    @classmethod
    def setUpClass(cls):
        """ Getting everything ready """
        cls.ins = Review()

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
        self.assertEqual(hasattr(self.ins, "place_id"), True)
        self.assertEqual(hasattr(self.ins, "user_id"), True)
        self.assertEqual(hasattr(self.ins, "text"), True)

    def test_isinstance(self):
        """ testing the instance """
        self.assertTrue(isinstance(self.ins, Review))

if __name__ == '__main__':
    unittest.main()
