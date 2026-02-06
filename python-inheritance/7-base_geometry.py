#!/usr/bin/python3
"""
Defines a class BaseGeometry.
"""


class BaseGeometry:
    """
    A class BaseGeometry based on 6-base_geometry.
    """
    def area(self):
        """
        Public instance method that raises an Exception with the message:
            "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
