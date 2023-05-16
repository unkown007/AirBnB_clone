#!/usr/bin/python3
""" unittest for the amenity class """


import unittest
from models.amenity import Amenity
import os


class TestAmenity(unittest.TestCase):
    """ Test Cases """

    @classmethod
    def setUpClass(cls):
        """ Getting everything ready """
        cls.ins = Amenity()


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
        self.assertEqual(hasattr(self.ins, "name"), True)

    def test_isinstance(self):
        """ testing the instance """
        self.assertTrue(isinstance(self.ins, Amenity))

if __name__ == '__main__':
    unittest.main()
