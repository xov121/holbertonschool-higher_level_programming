#!/usr/bin/python3
"""
Module that contains the to_json_string function.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj (Any): The object to serialize to a JSON string.

    Returns:
        str: JSON representation of my_obj.
    """
    return json.dumps(my_obj)
