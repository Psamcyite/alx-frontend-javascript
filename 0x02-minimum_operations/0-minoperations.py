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

    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = i
        for j in range(2, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]

# Test cases
if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

