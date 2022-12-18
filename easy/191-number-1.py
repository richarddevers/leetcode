# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/
# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Example 1:
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

# Example 2:
# Input: n = 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

# Example 3:
# Input: n = 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

import pytest


def count(s1: str) -> int:
    return len([char for char in list(s1) if char == "1"])


@pytest.mark.parametrize(
    "s1,expected",
    [
        ("00000000000000000000000000001011", 3),
        ("00000000000000000000000010000000", 1),
        ("11111111111111111111111111111101", 31),
    ],
)
def test_count(
    s1: str,
    expected: int,
) -> None:

    result = count(
        s1=s1,
    )

    assert result == expected
