#!/usr/bin/python3

def minOperations(n):
    """
    Calculate the minimum number of operations to reach exactly `n`
    characters using only "Copy All" and "Paste".

    Args:
    - n (int): The target number of characters to achieve.

    Returns:
    - int: Minimum number of operations required to achieve `n` characters.
    Returns 0 if `n` is impossible to achieve.
    """
    if n <= 1:
        return 0

    # Initialize a DP array where dp[i] will store the minimum operations to
    # reach i characters
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # Base case: 1 character requires 0 operations

    # Fill the dp array for all i from 2 to n
    for i in range(2, n + 1):
        # Try all possible lengths j such that j divides i
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                # If j divides i, then we can copy all characters up
                # to length j and paste (i//j - 1) times
                dp[i] = min(dp[i], dp[j] + (i // j))

    # If dp[n] is still infinity, it means it's impossible
    # to reach exactly n characters
    return dp[n] if dp[n] != float('inf') else 0
