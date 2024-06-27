#!/usr/bin/python3
"""
0-pascal_triangle.py - <This module defines a function that
returns a list of integers
representing the Pascal's Triangle of 'n'>
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of Pascal's triangle

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            row.append(row[-1] * (i - j + 1) // j)
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
