#!/usr/bin/python3
"""Square Module - Defines a Square class"""

from typing import Any
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square class."""

    def __init__(self, size: int):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides.
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self) -> int:
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self) -> str:
        """
        Generates a string representation of the square.

        Returns:
            str: A string describing the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
