#!/usr/bin/python3
"""
Module that contains the class Square, which inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A subclass of Rectangle that represents a square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides, must be a positive
                        integer.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns the square description.
        """
        return f"[Square] {self.__size}/{self.__size}"
