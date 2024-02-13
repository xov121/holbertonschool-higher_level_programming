#!/usr/bin/python3
"""
Module 6-rectangle
Defines a class Rectangle with a class attribute to count instances,
methods to calculate its area and perimeter,
a method to represent the rectangle using the character #,
a repr method to recreate a new instance with eval(),
and a custom deletion message.
"""


class Rectangle:
    """Class that defines a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Returns the area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the Rectangle.
        Returns 0 if either the width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the Rectangle.
        Represents the rectangle with rows of # characters.
        Returns an empty string if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rows = ["#" * self.width for _ in range(self.height)]
        return "\n".join(rows)

    def __repr__(self):
        """Returns a string representation of the rectangle for eval().
        This allows recreation of a new instance with the same attributes.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted
        and decrements the instance counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
