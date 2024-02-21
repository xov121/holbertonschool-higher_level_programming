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
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance,
        potentially filtered by a list of attributes.
        Args:
            attrs (list of str): The list of attributes to include in the
                                 returned dictionary. If None, all attributes
                                 are included.
        Returns:
            dict: A dictionary representation of the Student instance,
                  filtered by attrs if provided.
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            filtered_dict = {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
            return filtered_dict
        return self.__dict__
