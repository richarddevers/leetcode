# https://leetcode.com/problems/longest-consecutive-sequence/

# 128. Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
import typing as t

import pytest

# def longest(nums: t.List[int]) -> int:
#     """
#     Sorting, 0(nlogn) (sorting is long)
#     """

#     sorted_nums = sorted(nums)

#     res = 1
#     tmp_result = []
#     for i in range(len(sorted_nums) - 1):
#         if sorted_nums[i] + 1 == sorted_nums[i + 1]:
#             res += 1
#         else:
#             tmp_result.append(res)
#             res = 1
#     return max(tmp_result)


# def test_longest():
#     nums = [100, 4, 200, 1, 3, 2]
#     expected = 4

#     result = longest(nums=nums)

#     assert result == expected


def longest2(nums: t.List[int]) -> int:
    nums_set = nums
    longest = 0

    for n in nums:
        # check if start of a sequence
        if n - 1 not in nums_set:
            length = 0
            while n + length in nums_set:
                length += 1
            longest = length if length > longest else longest
    return longest


def test_longest2():
    nums = [100, 4, 200, 1, 3, 2]
    expected = 4

    result = longest2(nums=nums)

    assert result == expected
