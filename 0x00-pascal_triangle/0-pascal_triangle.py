#!/usr/bin/python3
"""
0-pascal_triangle.py - This module defines a function that
returns a list of lists of integers
representing Pascal's Triangle of 'n'.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        List[List[int]]: A list of lists of integers
        representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of Pascal's triangle

    for i in range(1, n):
        # Use list comprehension to generate each row
        row = [1] + [
            triangle[i - 1][j - 1] + triangle[i - 1][j]
            for j in range(1, i)
        ] + [1]
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Prints Pascal's Triangle.

        Args:
            triangle (List[List[int]]): The Pascal's Triangle to print.
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
