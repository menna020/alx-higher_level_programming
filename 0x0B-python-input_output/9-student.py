#!/usr/bin/python3
"""The program defines a class student"""

class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """InitializeS a new Student

        Args:
            first_name (str): The student’s first name
            last_name (str): The student’s last name
            age (int): The student’s age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of the student"""
        return self.__dict__
