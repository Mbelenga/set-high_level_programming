#!/usr/bin/python3


"""A function that appends a string"""


def append_write(filename="", text=""):
    """
    A function that appends a string at the end of a textfile
    (UTF8) and returns the number of characters added
    """
    with open(filename, 'a') as file:
        return file.write(text)
