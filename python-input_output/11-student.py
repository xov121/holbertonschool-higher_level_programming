#!/usr/bin/python3
"""
Module that contains the Student class.
"""


class Student:
    """
    Defines a student by: first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance,
        potentially filtered by a list of attributes.
        """
        if attrs is not None and all(isinstance(a, str) for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from
        a JSON dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
