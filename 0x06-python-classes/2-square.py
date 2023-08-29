#!/usr/bin/python3
"""
This module defines a class called Square.
"""


class Square:
    """
    This class represents a square shape.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class
        Args:
        size (int): The side length of the square.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size
