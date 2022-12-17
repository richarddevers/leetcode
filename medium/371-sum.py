# 371. Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/

# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# Example 1:
# Input: a = 1, b = 2
# Output: 3

# Example 2:
# Input: a = 2, b = 3
# Output: 5

import pytest


def sum(
    a: int,
    b: int,
) -> int:
    return a ^ b


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (4, 211, 215),
        (1, 2, 3),
        (0, 2, 2),
        (0, 0, 0),
        (-1, -2, -3),
    ],
)
def test_sum(
    a: int,
    b: int,
    expected: int,
) -> None:
    a = 1
    b = 2
    expected = 3

    result = sum(
        a=a,
        b=b,
    )

    assert result == expected
