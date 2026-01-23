#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Function Description:
    - Adds 2 integers.
    - Prototype: def add_integer(a, b=98).
    - a and b must be integers or floats, otherwise,
        raise a TypeError exception with the message:
        "a must be an integer" or "b must be an integer".
    - a and b must be first casted to integers if they are float.

    Parameters:
    - a: first integer.
    - b: second integer = 98 (by default).

    Returns:
    - An integer from the addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
    