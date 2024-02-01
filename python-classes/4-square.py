#!/usr/bin/python3
"""
This module defines the `Square` class.

The `Square` class now includes a getter and setter for the `size` attribute
with proper validation. The class allows calculation of the square's area and
ensures that the `size` attribute is always a non-negative integer. This class
is part of a project focused on learning object-oriented programming (OOP) and
understanding the basics of class creation, attributes, methods, encapsulation,
and property decorators in Python.

Classes:
    Square: Defines a square with validated size, the ability to calculate its
        area, and access its size attribute via a property decorator.
"""


class Square:
    """
    A class that defines a square by its size with validation and can calculate
        its area.

    The `size` attribute is private and accessed or modified through a property
    decorator, ensuring it's always a non-negative integer.

    Attributes:
        size (int): The size of the square's side.
    """

    def __init__(self, size=0):
        """
        Initializes the square with size, enforcing that size is an integer and
                >= 0.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
