#!/usr/bin/python3
"""
This module defines the `Square` class.

The `Square` class now includes a `position` attribute that controls where the
square is printed. The class allows calculation of the square's area, ensures
that the `size` attribute is always a non-negative integer, provides a textual
representation of the square, and respects its position for printing. This
class is part of a project focused on learning object-oriented programming
(OOP) and understanding the basics of class creation, attributes, methods,
encapsulation, property decorators, and textual representation of objects in
Python with respect to their position.

Classes:
    Square: Defines a square with validated size and position, the ability to
    calculate its area, access its size and position attributes via property
    decorators, and visually represent itself respecting its position.
"""


class Square:
    """
    A class that defines a square by its size with validation, can calculate
        its area, and visually represent itself respecting its position.

    The `size` and `position` attributes are private and accessed or modified
        through property decorators, ensuring the size is always a non-negative
                integer and the position is a tuple of 2 positive integers.

    Attributes:
        size (int): The size of the square's side.
        position (tuple): The position of the square for printing.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with size and position, enforcing that size is
                an integer and >= 0 and position is a tuple of 2 positive
                                integers.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults
                        to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
            The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the `#` character respecting its position.
        """
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
