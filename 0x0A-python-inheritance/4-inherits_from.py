#!/usr/bin/python3
"""
A module for the function inherits_from
"""


def inherits_from(obj, a_class):
    """
    Check if an object inherits
    (directly or indirectly) from a specified class.

    Args:
        obj (object): The object to be checked.
        a_class (class): The class to be checked against.

    Returns:
    bool: True if obj is an instance of a class
        that inherits from a_class, False otherwise.
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
