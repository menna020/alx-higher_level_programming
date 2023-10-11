#!/usr/bin/python3
"""This module defines a function that reads text files"""


def read_file(filename=""):
    """
    This function reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to be read with a default of an empty string.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
            print(file.read(), end="")
