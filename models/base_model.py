#!/usr/bin/python3
"""Module that  defines the base model for all the classes"""


from uuid import uuid4
from datetime import datetime
import models


time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    BaseModel class that implements neccessary features for the future class
    """

    def __init__(self, *args, **kwargs):
        """Initialize all objects attributes
        Args:
            *args(list): non keyworded list of arguments
            **kwargs(dict): keyworded arguments
        """
        if args is not None and len(args) > 0:
            pass
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, time_format)
                if key not in ['__class__']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.updated_at = self.created_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self);
        models.storage.save();

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        dic = {}

        for key, value in self.__dict__.items():
            if key not in ['created_at', 'updated_at']:
                dic[key] = value
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        dic['id'] = self.id
        return dic

    def __str__(self):
        """Return a printable string of the object"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)
