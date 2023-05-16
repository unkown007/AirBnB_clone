#!/usr/bin/python3
""" unittest for the amenity class """


import unittest
from models.user import User
import os


class TestAmenity(unittest.TestCase):
    """ Test Cases """

    @classmethod
    def setUpClass(cls):
        """ Getting everything ready """
        cls.ins = User()


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
        self.assertEqual(hasattr(self.ins, "email"), True)
        self.assertEqual(hasattr(self.ins, "password"), True)
        self.assertEqual(hasattr(self.ins, "first_name"), True)
        self.assertEqual(hasattr(self.ins, "last_name"), True)

    def test_isinstance(self):
        """ testing the instance """
        self.assertTrue(isinstance(self.ins, User))

if __name__ == '__main__':
    unittest.main()
