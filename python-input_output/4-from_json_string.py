#!/usr/bin/python3
"""
Module that contains the from_json_string function.
"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        The Python object represented by the JSON string.
    """
    return json.loads(my_str)
