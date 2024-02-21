#!/usr/bin/python3
"""
 Returns a list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Args:
        obj: The object to list attributes and methods for.

    Returns:
        A list object containing the names of the object's attributes and
        methods.
    """
    return dir(obj)
