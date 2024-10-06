#!/usr/bin/python3
"""
Module to calculate the minimum number of operations needed
to achieve exactly n H characters in a text file.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters.

    Parameters:
    n (int): The target number of characters.

    Returns:
    int: The minimum number of operations needed, or 0 if impossible.
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    # Prime factorization logic
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
