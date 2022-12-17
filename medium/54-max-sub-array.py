# https://leetcode.com/problems/maximum-subarray/


# Given an integer array nums, find the
# subarray
#  which has the largest sum and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

import typing as t


def maxi(
    nums: t.List[int],
) -> int:
    max_sub = nums[0]
    current_sum = 0

    for n in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += n
        max_sub = max(max_sub, current_sum)
    return max_sub


def test_max() -> None:
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = 6

    result = maxi(
        nums=nums,
    )

    assert result == expected
