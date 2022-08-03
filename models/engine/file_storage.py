#!/usr/bin/python3
"""
This module contains FileStorage class
"""
import json


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        self.__objects.update({f'{type(obj).__name__}.\
                {obj.id}': obj.to_dict()})

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                self.__objects = json.loads(f.read())
        except Exception:
            self.__objects = {}
