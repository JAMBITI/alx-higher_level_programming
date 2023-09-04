#!/usr/bin/python3
"""
Matrix Division Module
"""


def matrix_divided(matrix, div):
    """
Divide all elements of a matrix by a number.

Args:
        matrix (list of lists): The input matrix.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with
        elements rounded to two decimal places.

    Raises:
TypeError: If matrix is not a list of lists containing only integers or floats,
or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Error Messages
    matrix_type_error = "matrix must be a matrix
    (list of lists) of integers/floats"
    row_size_error = "Each row of the matrix must
    have the same size"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is list:
        if len(matrix) == 0:
            raise TypeError(matrix_type_error)

        for row in matrix:
            if type(row) is not list:
                raise TypeError(matrix_type_error)

            length = len(matrix[0])
            if len(row) != length:
                raise TypeError(row_size_error)

            for element in row:
                if not isinstance(element, (int, float)):
                    raise TypeError(matrix_type_error)
    else:
        raise TypeError(matrix_type_error)

    new_matrix = []

    for row in matrix:
        new_row = []

        for element in row:
            new_row.append(round((element / div), 2))

        new_matrix.append(new_row)

    return new_matrix
