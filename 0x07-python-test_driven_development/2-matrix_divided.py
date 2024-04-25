#!/usr/bin/python3
"""
Modile 2-matrix_divided
contain one method that divided the element of
The same size of int or float matrix
Return the devidened number rouneded to two decimal place
"""

def matrix_divided(matrix, div):
    """Return new matrix with devidedned"""

    errorMessage = "matrix must be a matrix (list of lists) of integers/floats"
    message_one = "Each row of the matrix must have the same size"

    if not matrix:
        raise TypeError(errorMessage)
    if not isinstance(matrix, list):
        raise TypeError(errorMessage)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(errorMessage)
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(errorMessage)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(errorMessage)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in lists] for lists in matrix]
