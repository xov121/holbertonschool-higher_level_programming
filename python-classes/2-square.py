#!/usr/bin/python3
"""
This module defines the `Square` class.

The `Square` class is now enhanced to include validation for the
`size` attribute. The size must be an integer and must be >= 0.
This class is part of a project focused on learning object-oriented
programming (OOP) and understanding the basics of class creation,
attributes, methods, and encapsulation in Python.

Classes:
    Square: Defines a square with validated size.
"""


class Square:
    """
    A class that defines a square by its size with validation.

    Attributes:
        size (int): The size of the square's side.

    The `size` attribute is private and validated to ensure it's an integer and
    that it's >= 0.
    """

    def __init__(self, size=0):
        """
        Initializes the square with size, enforcing that size is an
                integer and >= 0.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
