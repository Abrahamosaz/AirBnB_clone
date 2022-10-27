#!/usr/bin/env python3
import models
import uuid
import datetime
"""
    BaseModel inherit by all other models
"""


class BaseModel:
    """
    Basemodel for all other models in the database
    """

    def __init__(self, *args, **kwargs):
        """
        initailize the instance atrributes
        Args:
            id: string id of easch instances

            created_at: the current date and time the instance was
            created

            updated_at: The updated date and time everytime instance
            object is change
        """
        if kwargs:
            name = ["updated_at", "created_at"]
            for key, value in kwargs.items():
                if key not in name and key != "__class__":
                    setattr(self, key, value)
                elif key in name:
                    value_dt = datetime.datetime.fromisoformat(value)
                    setattr(self, key, value_dt)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        return the string representation of the instance object
        """
        return ("[" + self.__class__.__name__ + "] " +
                "(" + self.id + ") " + str(self.__dict__))

    def save(self):
        """
        update the current instance atrribute (updated_at)
        with the current date and time
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        return the key/value  of the instance object
        """
        new_dict = {}

        for key, value in self.__dict__.items():
            new_dict[key] = value
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return (new_dict)
