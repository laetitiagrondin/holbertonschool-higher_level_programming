#!/usr/bin/python3
"""
Defines a class Student that defines a student.
"""


class Student:
    """
    class Student that defines a student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation with public instance attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary representation
        of a Student instance.
        If attrs is a list of strings,
        only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved.
        """
        if (isinstance(attrs, list) and
           all(isinstance(key, str) for key in attrs)):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
