#!/usr/bin/python3
"""
Module that contains the class Rectangle, which inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A subclass of BaseGeometry that represents a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle, must be a positive
                         integer.
            height (int): The height of the rectangle, must be a positive
                          integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
