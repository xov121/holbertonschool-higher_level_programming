#!/usr/bin/python3
"""
Module that contains the load_from_json_file function.
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a "JSON file".

    Args:
        filename (str): The name of the file to read from.

    Returns:
        The Python object represented by the JSON string in the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
