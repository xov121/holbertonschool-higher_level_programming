#!/usr/bin/python3
class Square:
    """Square class with a private instance attribute size with validation"""

    def __init__(self, size=0):
        """Initialize a new square with size validation.
        Args:
            size (int): The size of the new square,
                        must be an integer and >= 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
