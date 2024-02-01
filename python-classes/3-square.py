#!/usr/bin/python3
class Square:
    """Square class: represents a square
        with a private instance attribute size."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square,
                        must be an integer and >= 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
