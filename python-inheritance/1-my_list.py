#!/usr/bin/python3
"""
Defines a class My_List.
"""


class MyList(list):
    """
    A class MyList that inherits from list.
    """
    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort).
        """
        self.sort()
        print(self)
