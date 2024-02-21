#!/usr/bin/python3
"""
Module that contains the class BaseGeometry.
"""


class BaseGeometry:
    """
    A class BaseGeometry with public instance method area and
    integer_validator.
    """

    def area(self):
        """
        Raises an Exception with a message indicating that the method is not
        yet implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.

        Args:
            name (str): The name of the value (primarily used in error
                        messages).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
