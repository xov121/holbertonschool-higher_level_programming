#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to list attributes and methods for.

    Returns:
        A list object containing the names of the ibject's attributes and
        methods.
    """
    return dir(obj)
