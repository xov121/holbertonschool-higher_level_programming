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
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.
        Args:
            value (int): The new size of the square,
                        must be an integer and >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
