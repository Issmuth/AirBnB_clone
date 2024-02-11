#!/usr/bin/python3
""" Base Class Definition module."""
from datetime import datetime
import models
import uuid


form = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """All underlying classes will be based
    on this base class.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a base model instance.

        Args:
            args: arguments list (unused)
            kwargs: key/value pairs for attributes
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if (k == "created_at" or k == "updated_at"):
                    date = datetime.strptime(v, form)
                    self.__dict__[k] = datetime.strptime(v, form)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Prints the Class name, uuid and object."""
        str1 = "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
        return str1

    def save(self):
        """Updates the public instance updated_at with
        the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary with all key/values of __dict__."""
        temp_dict = self.__dict__.copy()
        temp_dict["__class__"] = self.__class__.__name__
        if "created_at" in temp_dict:
            temp_dict["created_at"] = self.created_at.isoformat()
        if "updated_at" in temp_dict:
            temp_dict["updated_at"] = self.updated_at.isoformat()

        return temp_dict
