#!/usr/bin/python3
"""Unittest for testing FileStorage"""

from contextlib import redirect_stdout
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import io
import os
import sys


class storageTest(unittest.TestCase):
    """Testing storage access"""

    def test_save(self):
        """test saving of new obj"""
        model = BaseModel()
        x = model.id
        y = "BaseModel.{}".format(x)
        model.save()
        with open("file.json", 'r', encoding="utf-8") as f:
            data = json.loads(f.read())
        self.assertEqual(y in data.keys(), True)

    def test_newobj(self):
        """test self.__ojects in filestorage"""
        storage = FileStorage()
        model = BaseModel()
        x = model.id
        y = "BaseModel.{}".format(x)
        storage.new(model)
        z = storage.all()
        self.assertEqual(y in z.keys(), True)

    def test_reload(self):
        """if file does not exist"""
        storage = FileStorage()
        os.rename('file.json', 'file2.json')
        storage.reload()
        z = storage.all()
        self.assertEqual(z, {})
        os.rename('file2.json', 'file.json')
