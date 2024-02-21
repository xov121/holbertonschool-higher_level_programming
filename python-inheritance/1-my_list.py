#!/usr/bin/python3
"""
Module that defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    A subclass of list that includes a method to print the list in ascending
    order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
