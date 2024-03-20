#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    n_row = len(matrix)
    n_col = len(matrix[0]) if matrix and len(matrix) > 0 else 0

    new_matrix = []
    for i in range(n_row):
        row = []
        for k in range(n_col):
            element = matrix[i][k]
            row.append(element ** 2)
        new_matrix.append(row)
    return (new_matrix)
