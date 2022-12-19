# 238. Product of Array Except Self

# https://leetcode.com/problems/product-of-array-except-self/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

import typing as t

import pytest


def prods(nums: t.List[int]) -> t.List[int]:
    results = []
    i = 0
    while i < len(nums):
        tmp = list(nums)
        tmp[i] = 1
        curr = 1
        for elt in tmp:
            curr *= elt
        results.append(curr)
        i += 1
    return results


@pytest.mark.parametrize(
    "nums,expected",
    [
        (
            [1, 2, 3, 4],
            [24, 12, 8, 6],
        ),
        (
            [-1, 1, 0, -3, 3],
            [0, 0, 9, 0, 0],
        ),
    ],
)
def test_prods(
    nums: t.List[int],
    expected: t.List[int],
) -> None:

    result = prods(
        nums=nums,
    )

    assert result == expected


##############


def prods2(nums: t.List[int]) -> t.List[int]:
    res = [1] * len(nums)

    prefix = 1
    for index, value in enumerate(nums):
        res[index] = prefix
        prefix *= value

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res


@pytest.mark.parametrize(
    "nums,expected",
    [
        (
            [1, 2, 3, 4],
            [24, 12, 8, 6],
        ),
        (
            [-1, 1, 0, -3, 3],
            [0, 0, 9, 0, 0],
        ),
    ],
)
def test_prods2(
    nums: t.List[int],
    expected: t.List[int],
) -> None:

    result = prods2(
        nums=nums,
    )

    assert result == expected
