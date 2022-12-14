# 1. Two Sum

# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target,
#  return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
#  and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

import typing as t

import pytest

test_data = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
]


def two_sum1(
    nums: t.List[int],
    target: int,
) -> t.List[int]:
    i = 0
    previous_value_index: t.Dict[int, int] = {}  # value->index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in previous_value_index:
            return [previous_value_index[diff], i]
        previous_value_index[n] = i


@pytest.mark.parametrize(
    "nums,target,expected",
    test_data,
)
def test_two_sum1(
    nums,
    target,
    expected,
) -> None:

    result = two_sum1(
        nums=nums,
        target=target,
    )

    assert result == expected
