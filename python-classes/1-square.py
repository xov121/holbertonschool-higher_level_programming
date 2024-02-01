#!/usr/bin/python3
"""
This module defines the `Square` class.

The `Square` class is a basic implementation of a square. In this
version, the class includes an initialization method that sets the
size of the square. This class is part of a project focused on
learning object-oriented programming (OOP) and understanding the
basics of class creation, attributes, methods, and encapsulation
in Python.

Classes:
    Square: Defines a square with size.
"""


class Square:
    """
    A class that defines a square by its size.

    Attributes:
        size (int): The size of the square's side.

    The `size` attribute is private, meaning it should be accessed and modified
    only through getters and setters (to be implemented in later tasks).

    At this point, the `size` attribute is initialized without any validation.
    """

    def __init__(self, size):
        """
        Initializes the square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
