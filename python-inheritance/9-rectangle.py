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
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the rectangle description.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
