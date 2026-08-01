#!/usr/bin/python3

"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """
    A Function that inserts a line of text to a file
    aftermeach line containing a specific string
    """
    with open(filename, "r") as file:
        text = file.readlines()

    with open(filename, "w") as file:
        string = ""
        for line in text:
            string += line
            if search_string in line:
                string += new_string
        file.write(string)
