#!/usr/bin/python3
"""Minimum number of coins needed to reach a given total"""


def makeChange(coins: list, total: int) -> int:
    """Return the fewest coins that sum to total or -1 if impossible"""

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount and dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    if dp[total] == float('inf'):
        return -1
    return dp[total]
