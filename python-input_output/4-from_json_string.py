#!/usr/bin/python3

"""Returns an object"""

import json
"""A function needed to convert"""


def from_json_string(my_str):
    """
    A function that returns a python data structure
    represented by a JSON string
    """
    return json.loads(my_str)
