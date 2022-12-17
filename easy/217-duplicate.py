# 217. Contains Duplicate


# https://leetcode.com/problems/contains-duplicate/

# Given an integer array nums, return true if any value appears at least twice in the array,
#  and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
import typing as t

import pytest


def duplicate(
    nums: t.List[int],
):
    return len(nums) != len(set(nums))


def duplicate2(
    nums: t.List[int],
):
    tmp: t.Dict[int, int] = {}
    for n in nums:
        if not tmp.get(n):
            tmp[n] = 1
        else:
            return True
    return False


def duplicate3(
    nums: t.List[int],
):
    return any([nums.count(n) > 1 for n in nums])


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ],
)
def test_duplicate(
    nums: t.List[int],
    expected: bool,
) -> None:
    result = duplicate3(
        nums=nums,
    )

    assert result == expected
