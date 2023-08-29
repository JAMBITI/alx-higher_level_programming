class Square:
    """
    A class definition for a square.
    """

    def __init__(self, size=0):
        """
        Initialize the instance attributes.

        Args:
            size (int): The side length of the square.
        """
        self._validate(size)
        self.__size = size

    @property
    def size(self):
        """
        Get the private variable size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the private variable size.

        Args:
            value (int): The side length of the square.
        """
        self._validate(value)
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character.
        """
        if self.__size > 0:
            for _ in range(self.__size):
                print("#" * self.__size)
        else:
            print("")

    def _validate(self, value):
        """
        Validate the input value.

        Args:
            value (int): Data to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
