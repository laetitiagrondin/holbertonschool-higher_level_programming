#!/usr/bin/python3
"""
Module that prints a person's name.
"""


def say_my_name(first_name, last_name=""):
    """
    Function Description:
    - Write a function that prints My name is <first name> <last name>
    - Prototype: def say_my_name(first_name, last_name="").
    - first_name and last_name must be strings, otherwise,
        raise a TypeError exception with the message:
        "first_name must be a string" or "last_name must be a string".

    Parameters:
    - first_name: a string and the first name of the person.
    - last_name: a string and the last name of the persone.

    Returns:
    - This function does not return.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name).strip())
