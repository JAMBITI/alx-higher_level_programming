class Square:
    """
    This class defines a square shape.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.
        
        Args:
            size (int): The size of the square.
        """
        self._Square__size = size

    @property
    def size(self):
        """
        Getter method for the size of the square.
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size of the square.
        
        Args:
            value (int): The new size value.
            
        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the input is negative.
        """
        if type(value) is not int:
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        else:
            self._Square__size = value

    def area(self):
        """
        Calculates the area of the square.
        
        Returns:
            int: The calculated area.
        """
        return self._Square__size ** 2

