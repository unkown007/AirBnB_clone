#!/usr/bin/python3
""" unittest """


import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import os


class TestBase(unittest.TestCase):
    """ test cases """

    @classmethod
    def setUpClass(cls):
        """ setup BaseModel instance"""
        cls.ins = BaseModel()

    @classmethod
    def teardown(cls):
        """ cleaning up all test working tools """
        del cls.ins
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_BaseModelAttr(self):
        """ Testing BaseModel attributes """
        self.assertEqual(hasattr(self.ins, 'id'), True)
        self.assertEqual(hasattr(self.ins, 'created_at'), True)
        self.assertEqual(hasattr(self.ins, 'updated_at'), True)

    def test_instance(self):
        """ Testing BaseModel instance """
        self.assertTrue(isinstance(self.ins, BaseModel))


    def test_save_updated_at_created_at(self):
        """ Testing the save updated_at and created_at attributes """
        self.ins.save()
        self.assertNotEqual(self.ins.created_at, self.ins.updated_at)
        dummy = BaseModel()
        id_t = dummy.id
        dummy.name = "Victor"
        dummy.save()
        storage.reload()
        obj = storage.all()[f"BaseModel.{id_t}"]
        self.assertTrue(hasattr(obj, "name"))
        self.assertTrue(obj.name == "Victor")
        self.assertTrue(os.path.exists("file.json"))

    def test_dic(self):
        """ Testing dictionary representation """
        dic = self.ins.to_dict()
        self.assertTrue(dic.get("__class__"))
        self.assertTrue(type(dic) is dict)
        self.assertTrue("to_dict" in dir(self.ins))

    def test_storage(self):
        """ Testing storage """
        objs = storage.all()

        self.assertTrue(type(objs) is dict)
        self.assertTrue(isinstance(storage, FileStorage))

    def test_reaload(self):
        """ Testing reload of objs in file.json """
        self.ins.save()
        storage.reload()
        dic = storage.all()
        self.assertTrue(len(dic) != 0)

    def test_str(self):
        """ Testing object string representation """
        self.assertTrue("__str__" in dir(self.ins))
        self.assertTrue(type(self.ins.__str__()) is str)

if __name__ == "__main__":
    unittest.main()
