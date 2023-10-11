#!/usr/bin/python3
"""The program defines a function that inserts a text file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing
    a given string in a file

    Args:
        filename (str): The file’s name
        search_string (str): The string to search in within the file
        new_string (str): The string to be inserted
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
