#!/usr/bin/python3
"""
Defines a class Square.
"""


class Square:
    """
    A class that represents a square with a private size attribute.
    """
    def __init__(self, size):
        """
        Funcion Description:
        - Initializes a Square instance with a private size attribute.

        Parameter:
        - size: an integer that is the size of the square.
        """
        self.__size = size
