#!/usr/bin/python3
"""The program defines a class student
   based on 9-student.py"""

class student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student

        Args:
            first_name (str): The student’s first name
            last_name (str): The student’s last name
            age (int): The student’s age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the student

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to be represented
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
