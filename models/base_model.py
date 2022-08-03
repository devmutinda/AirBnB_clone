#!/usr/bin/python3
"""
This module contains Basemodel class
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Defines all common attributes for other classes
    """
    name = None
    my_number = None

    def __init__(self, *args, **kwargs):
        """Instance constructor"""
        if (kwargs):
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns string rep of instance"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates attribute updated_at with current datetime"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        return {
                'my_number': self.my_number,
                '__class__': type(self).__name__,
                'name': self.name,
                'updated_at': datetime.isoformat(self.updated_at),
                'id': self.id,
                'created_at': datetime.isoformat(self.created_at)
                }
