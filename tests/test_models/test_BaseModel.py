#!/usr/bin/python3
"""Unittest for BaseModel"""

from contextlib import redirect_stdout
import unittest
from models.base_model import BaseModel
from datetime import datetime
import io
import os
import sys


class baseTest(unittest.TestCase):
    """Class that tests BaseModel"""

    def test_init(self):
        """test initialisation"""
        model = BaseModel()
        self.assertEqual(model.name, None)
        self.assertEqual(model.my_number, None)

    def test_init2(self):
        """test initialisation"""
        model = BaseModel()
        model.name = "Test"
        model.my_number = 29
        self.assertEqual(model.name, "Test")
        self.assertEqual(model.my_number, 29)
    def test_initkwargs(self):
        """test init with kwargs"""
        model = BaseModel(name = 'Test', my_number = 30)
        self.assertEqual(model.name, 'Test')
        self.assertEqual(model.my_number,30)

    def test_initid(self):
        """test allocation of uuid"""
        model = BaseModel()
        self.assertEqual(type(model.id), str)
        self.assertEqual(len(model.id), 36)

    def test_initdate(self):
        """test datetime"""
        model = BaseModel()
        x = str(datetime.now())[:-10]
        y = str(model.created_at)[:-10]
        z = str(model.updated_at)[:-10]
        self.assertEqual(x, y)

    def test_str(self):
        """test __str__"""
        model = BaseModel()
        model.name = "Test"
        model.my_number = 29
        output = ""
        with io.StringIO() as buf, redirect_stdout(buf):
            print(model)
            output = buf.getvalue()
        self.assertEqual(output[1:10], 'BaseModel')
        z = '\'my_number\': 29'
        x = z in output
        self.assertEqual(x, True)

    def test_save(self):
        """test update attr after/during save"""
        model = BaseModel()
        x = model.updated_at
        model.name = "Test"
        model.save()
        self.assertNotEqual(x, model.updated_at)
        self.assertEqual(str(x)[:-10], str(model.updated_at)[:-10])


if __name__ == '__main__':
    unittest.main()
