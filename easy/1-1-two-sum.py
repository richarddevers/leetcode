# 1. Two Sum SORTED
# https://www.youtube.com/watch?v=-gjxg6Pln50&t=7s&ab_channel=TeamAlgoDaily

# Given an array of SORTED integers nums and an integer target,
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


def two_sum2(
    nums: t.List[int],
    target: int,
) -> t.List[int]:
    # Input: nums = [2,7,11,15], target = 9
    # Output: [0,1]
    # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    left = 0
    right = len(nums) - 1
    nums.sort()
    while left < right:
        result = nums[left] + nums[right]

        if result == target:
            return [left, right]

        if result < target:
            left += 1
        else:
            right -= 1
    return []


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([2, 3, 4], 6, [0, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum2(
    nums,
    target,
    expected,
) -> None:

    result = two_sum2(
        nums=nums,
        target=target,
    )

    assert result == expected
