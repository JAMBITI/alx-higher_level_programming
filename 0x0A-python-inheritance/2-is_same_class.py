#!/usr/bin/python3
"""Defines a function for class type comparison."""



def is_same_class(obj, a_class):
"""Check if an object is an instance of a given class.

Args:
obj (any): The object to check.
a_class (type): The class to compare with the type of obj.

Returns:
bool: True if obj is an instance of a_class, False otherwise.
    """


return isinstance(obj, a_class)
