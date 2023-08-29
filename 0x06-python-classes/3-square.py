#!/usr/bin/python3
"""
This script defines a class called Square for geometric calculations.
"""


class Square:
    """
    Represents a geometric square.

    Attributes:
        __size (int): The size of the square's sides.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
        size (int): The size of the square's sides.
        Must be a non-negative integer.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is a negative integer.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
