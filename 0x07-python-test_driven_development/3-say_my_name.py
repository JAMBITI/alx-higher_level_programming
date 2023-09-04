#!/usr/bin/python3
"""
A module for saying names.
"""


def say_my_name(first_name, last_name=""):
    """
    Print a formatted name string.

    :param first_name: The first name.
    :param last_name: The last name (default is '').
    :raises TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
