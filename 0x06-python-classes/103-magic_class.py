#!/usr/bin/python3
"""
This script defines the MagicClass class for working with circles.
"""


import math


class MagicClass:
    """
    A class that represents a circle and provides methods
    for area and circumference calculations.
    """
    def __init__(self, radius=0):
        """
        Initializes a circle with the given radius.

        :param radius: The radius of the circle.
        :type radius: int or float
        :raises TypeError: If the radius is not a number.
        """
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        :return: The area of the circle.
        :rtype: float
        """
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        :return: The circumference of the circle.
        :rtype: float
        """
        return (math.pi * 2) * self._MagicClass__radius
