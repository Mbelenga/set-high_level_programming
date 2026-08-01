#!/usr/bin/python3

"""A function that writes an object to a text file"""

import json
"""functions needed to convert"""


def save_to_json_file(my_obj, filename):
    """
    A function that writes an object to a text file
    using JSON representation
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
