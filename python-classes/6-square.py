#!/usr/bin/python3
"""
Defines a class Square.
"""


class Square:
    """
    A class that represents a square with a private size attribute.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Function Description:
        Initializes a Square instance with a
            private size and position attributes.

        Parameters:
        - size: an integer that is the size of the square, 0 by default.
        - position: a tuple that is the position of the square,
            (0, 0) by default.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Function Description:
        - Retrieves the size of the square.

        Returns:
        - The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Function Description:
        - Validates the type and value of size, otherwise:
            - Raises a TypeError exception with the message:
            "size must be an integer".
            - Raises a ValueError exception with the message:
            "size must be >= 0".

        Parameter:
        - value: The new size to assign to the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Function Description:
        - Retrieves the position of the square.

        Returns:
        - The position of the square as a tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Function Description:
        - Validates that 'tuple' is a tuple of 2 positive integers, otherwise:j
            - Raises a TypeError exception with the message:
                "position must be a tuple of 2 positive integers".

        Parameter:
        - value: The new size to assign to the square.
        """
        if (not isinstance(value, tuple) and len(value) != 2 or
           not isinstance(value[0], int) and value[0] < 0 or
           not isinstance(value[1], int) and value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Function Description:
        - Calculates the area using the formula:
            area = size^2

        Returns:
        - The current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Function Description:
        - Prints the square using the '#' character considering its position.
        - If size is equal to 0, it prints an empty line.
        """
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
