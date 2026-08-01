#!/usr/bin/python3
"""This module supplies one function, matrix_divided.

matrix_divided(matrix, div) divides every element of a matrix by div
and returns a new matrix with the results rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with all elements divided by div.

    Every result is rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(msg)
        for element in row:
            if not isinstance(element, (int, float)) or \
                    isinstance(element, bool):
                raise TypeError(msg)
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
