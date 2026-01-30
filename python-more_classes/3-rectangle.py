#!/usr/bin/python3
"""
Defines a class Rectangle.
"""


class Rectangle:
    """
    A class that represents a rectangle with
    private width and height attributes.
    """
    def __init__(self, width=0, height=0):
        """
        Function Description:
        - Initializes a Rectangle instance with width and height attributes.

        Parameters:
        - width: an integer representing the width of the rectangle.
        - height: an integer representing the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Function Description:
        - Retrieves the width of the rectangle.

        Returns:
        - The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Function Description:
        - Validates the type and value of width, if not:
            - Raise a TypeError exception with the message:
                "width must be an integer"
            - Raise a ValueError exception with the message:
                "width must be >= 0"

        Parameters:
        - value: the new size to assign to the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Function Description:
        - Retrieves the width of the rectangle.

        Returns:
        - The width of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Function Description:
        - Validates the type and value of height, if not:
            - Raise a TypeError exception with the message:
                "height must be an integer"
            - Raise a ValueError exception with the message:
                "height must be >= 0"

        Parameters:
        - value: the new size to assign to the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Function Description:
        - Calculates the area using the formula:
            area = height * width

        Returns:
        - The rectangle area.
        """
        return self.height * self.width

    def perimeter(self):
        """
        Function Description:
        - Calculates the perimeter using the formula:
            perimeter = 2 * (width * height)

        Returns:
        - The rectangle perimeter.
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Function Description:
        - Prints the rectangle using the '#' character.

        Returns:
        - A string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)
