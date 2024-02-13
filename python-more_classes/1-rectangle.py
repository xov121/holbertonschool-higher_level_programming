#!/usr/bin/python3
"""
Module 1-rectangle
Defines a class Rectangle with private instance attributes width and height,
and property and setter methods for width and height.
"""


class Rectangle:
    """Class that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle.
        Args:
            value (int): The new width of the rectangle.
        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle.
        Args:
            value (int): The new height of the rectangle.
        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
