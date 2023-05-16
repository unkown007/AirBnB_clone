#!/usr/bin/python3
""" unittest """


import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """ Test Cases """
    
    @classmethod
    def setUpClass(cls):
        """ getting everything ready """
        cls.ins = FileStorage()

    @classmethod
    def teardown(cls):
        """ cleaning everything """
        del cls.ins
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_FileStorsageAttr(self):
        """ test basemodel attributes """
        self.assertEqual(hasattr(self.ins, "_FileStorage__file_path"), True)
        self.assertTrue(type(self.ins._FileStorage__file_path) is str)
        self.assertEqual(hasattr(self.ins, "_FileStorage__objects"), True)

    def test_isinstanceofFileStorage(self):
        self.assertTrue(isinstance(self.ins, FileStorage))

    def test_allFS(self):
        my_dict = self.ins.all()
        self.assertTrue(type(my_dict) is dict)

    def test_saveFS(self):
        dummy = BaseModel()
        my_id = dummy.id
        dummy.name = "Haroldo"
        dummy.save()
        storage.reload()
        my_objs = storage.all()["BaseModel.{}".format(my_id)]
        self.assertTrue(hasattr(my_objs, "name"))
        self.assertTrue(my_objs.name == "Haroldo")
        self.assertTrue(os.path.exists('file.json'))

    def test_newFS(self):
        l1 = len(storage.all())
        dummy = BaseModel()
        l2 = len(storage.all())
        self.assertEqual(l1, l2 - 1)

if __name__ == '__main__':
    unittest.main()
