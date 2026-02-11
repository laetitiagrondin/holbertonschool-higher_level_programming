#!/usr/bin/python3
"""
Defines a function to_json_string that
returns the JSON representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string).
    """
    return json.dumps(my_obj)
