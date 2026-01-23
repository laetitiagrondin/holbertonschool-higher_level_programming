#!/usr/bin/python3
"""
Module to find the max integer in a list.
"""


def max_integer(list=[]):
    """
    If the list is empty, the function returns None
    Function Description:
    - Find the max integer in a list of integers.

    Parameters:
    - list: list of integers
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
