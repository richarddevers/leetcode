# 322. Coin Change

# https://leetcode.com/problems/coin-change/

# You are given an integer array coins representing coins of different denominations
#  and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

import typing as t

import pytest


def coinss(
    coins: t.List[int],
    amount: int,
) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    breakpoint()
    for amm in range(1, amount + 1):
        for coin in coins:
            breakpoint()
            if amm - coin >= 0:
                dp[amm] = min(dp[amm], 1 + dp[amm - coin])
    breakpoint()
    return dp[amount] if dp[amount] != amount + 1 else -1


def test_coins() -> None:
    coins = [1, 2, 5]
    amount = 11
    expected = 3

    result = coinss(
        coins=coins,
        amount=amount,
    )

    assert result == expected
