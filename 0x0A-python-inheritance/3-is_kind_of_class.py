#!/usr/bin/python3
"""
This module defines a function to check if an object is an instance
of, or if it inherits from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
Check if an object is an instance of, or if it inherits from,
the specified class.

Args:
obj: The object to be checked.
a_class: The class to be checked against.

Returns:
True if obj is an instance of or inherits from a_class, else False.
"""


return isinstance(obj, a_class)
