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

import pytest


def climbing1(
    height: int,
) -> int:
    """
    Brute force - dfs approach
    O(2^n)
    """
    result = 0
    dfs_call = []

    def dfs(
        current: int,
        step: int,
        result: int,
    ) -> int:
        dfs_call.append(True)
        current += step
        if current == height:
            result += 1
            return result

        if current > height:
            return result

        res_1 = dfs(
            current=current,
            step=1,
            result=result,
        )

        res_2 = dfs(
            current=current,
            step=2,
            result=result,
        )

        return res_1 + res_2

    res_1 = dfs(
        current=0,
        step=1,
        result=result,
    )
    res_2 = dfs(
        current=0,
        step=2,
        result=result,
    )
    print(f"dfs_call:{len(dfs_call)}")

    return res_1 + res_2


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
