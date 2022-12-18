# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

import typing as t

import pytest


def climbing1(
    height: int,
) -> int:
    """
    DP approache. Kind of fibonnacci
    """
    one, two = 1, 1

    for _ in range(height - 1):
        tmp = one
        one = one + two
        two = tmp
    return one


@pytest.mark.parametrize(
    "height,expected",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
    ],
)
def test_climbing1(
    height: int,
    expected: int,
) -> None:
    result = climbing1(
        height=height,
    )

    assert result == expected
