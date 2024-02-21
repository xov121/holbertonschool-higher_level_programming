#!/usr/bin/python3
"""
Module containing the class_to_json function.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON
    serialization of an object.

    Args:
        obj (Any): The object to serialize.

    Returns:
        dict: The dictionary representation of obj's __dict__.
    """
    return obj.__dict__
