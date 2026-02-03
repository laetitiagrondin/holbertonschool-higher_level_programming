#!/usr/bin/python3
"""
Defines a class Rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry (7-base_geometry),
    based on 8-rectangle.
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height.
        width and height must be private. No getter or setter.
        width and height must be positive integers,
            validated by integer_validator.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the rectangle area.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
