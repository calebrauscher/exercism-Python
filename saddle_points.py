"""Detect saddle points in a matrix."""

from typing import List


def saddle_points(matrix: List[List[int]]):
    """Return a list of dictionaries with row and col of saddle points

    Args:
        matrix (List[List[int]]): 2d matrix as a list of lists

    Raises:
        ValueError: raise ValueError if matrix is irregular

    Returns:
        [List[Dict[str, int]]]: list of dictionaries with row and col of saddle points
    """
    result = []

    if len(matrix) > 0:
        if is_matrix_irregular(matrix):
            raise ValueError("Invalid Matrix. Matrix must be regular.")

        row_max = [float("-inf")] * len(matrix)
        col_min = [float("inf")] * len(matrix[0])

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                row_max[row] = max(row_max[row], matrix[row][col])
                col_min[col] = min(col_min[col], matrix[row][col])

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == row_max[row] == col_min[col]:
                    result.append({"row": row + 1, "column": col + 1})

    return result


def is_matrix_irregular(matrix: List[List[str]]):
    """Return True if the matrix is irregular and False otherwise

    Args:
        matrix (List[List[str]]): 2d matrix as a list of lists

    Returns:
        [bool]: True if matrix is irregular and False otherwise
    """
    num_col = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != num_col:
            return True
    return False
