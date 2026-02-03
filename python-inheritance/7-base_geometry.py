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
        Public instance method that validates value:
            - if value is not an integer,
            raise a TypeError exception with the message:
                "<name> must be an integer".
            - if value is less or equal to 0,
            raise a ValueError exception with the message:
                "<name> must be greater than 0".
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
