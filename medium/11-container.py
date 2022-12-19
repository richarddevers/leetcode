# 11. Container With Most Water

# https://leetcode.com/problems/container-with-most-water/

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

import typing as t

import pytest


def contain(
    heights: t.List[int],
) -> int:
    # we want the two top , keep the smallest (if there's one) and multiply by the ditance
    amount = 0

    for index, value in enumerate(heights):
        if index == len(heights) - 1:
            break
        j = index + 1
        while j < len(heights):
            to_keep = value if value < heights[j] else heights[j]
            tmp = (j - index) * to_keep
            if tmp > amount:
                amount = tmp
            j += 1
    # for index, value in enumerate(heights):
    #     if index == len(heights) - 1:
    #         break
    #     j = index + 1
    #     while j < len(heights):
    #         to_keep = value if value < heights[j] else heights[j]
    #         tmp = (j - index) * to_keep
    #         if tmp > amount:
    #             amount = tmp
    #         j += 1
    return amount


@pytest.mark.parametrize(
    "heights,expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
    ],
)
def test_contain(
    heights,
    expected,
):

    result = contain(heights=heights)

    assert result == expected
