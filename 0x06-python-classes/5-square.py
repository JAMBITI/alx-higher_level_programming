#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Represents a square.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter for the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square.

        Args:
            value (int): The new size value.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#'.
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
