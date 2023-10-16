#!/usr/bin/python3
"""
Calculates the minimum number of operations needed to generate n H characters.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters.
    Args:
        n (int): The target number of H characters.
    Returns:
        int: The minimum number of operations.
    """
    if n <= 1:
        return n

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            n //= divisor
            operations += divisor
        divisor += 1

    return operations

# Test cases
if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

