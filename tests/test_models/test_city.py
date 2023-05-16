#!/usr/bin/python3
""" unittest for the class """


import unittest
from models.city import City
import os


class TestCity(unittest.TestCase):
    """ test cases """

    @classmethod
    def setUpClass(cls):
        """ getting everything ready for the test """
        cls.ins = City()

    @classmethod
    def teardown(cls):
        """ cleaning up everything """
        del cls.ins
        try:
            os.remove("file.json")
        except Exception:
            pass
    def test_BaseModelAttr(self):
        """ test base model attributes """
        self.assertEqual(hasattr(self.ins, "state_id"), True)
        self.assertEqual(hasattr(self.ins, "name"), True)

    def test_isinstance(self):
        """ testing the instance compatibility """
        self.assertTrue(isinstance(self.ins, City))

if __name__ == "__main__":
    unittest.main()
