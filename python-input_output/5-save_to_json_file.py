#!/usr/bin/python3
"""
Module that contains the save_to_json_file function.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Args:
        my_obj: The object to serialize and save.
        filename (str): The name of the file to write to.

    Note:
        Uses the 'with' statement to ensure proper handling of the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
