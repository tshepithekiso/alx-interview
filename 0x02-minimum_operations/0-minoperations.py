#!/usr/bin/python3

def minOperations(n):
    if n <= 1:
        return 0

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i  # Initialize with the maximum possible operations (i)

        j = 1
        while i * j <= n:
            dp[i * j] = min(dp[i * j], dp[i] + 1)
            j += 1

    return dp[n] if dp[n] != n else 0

