#!/usr/bin/python3
"""
This module defines a function to add two integers.
"""


def add_integer(a, b=98):

    """
    Adds two integers.

    :param a: The first integer.
    :param b: The second integer (default is 98).
    :raises TypeError: If a or b are not integers or floats.
    :return: The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
