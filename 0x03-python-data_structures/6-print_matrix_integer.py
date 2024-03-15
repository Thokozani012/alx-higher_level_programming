#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if not isinstance(matrix, list):
        return
    if not matrix:
        return
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix and len(matrix) > 0 else 0

    for i in range(num_rows):
        for k in range(num_cols):
            if k == num_cols - 1:
                print("{:d}".format(matrix[i][k]), end='')
            else:
                print("{:d}".format(matrix[i][k]), end=' ')
        print()
