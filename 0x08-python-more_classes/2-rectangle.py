#!/usr/bin/python3

class Rectangle:
    """A class representing a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("Width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        elif value < 0:
            raise ValueError("Height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.height * self.width

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
    if self.height > 0 and self.width > 0 else 0
    return 2 * (self.height + self.width)
