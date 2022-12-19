# 15. 3Sum
# https://leetcode.com/problems/3sum/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

import pytest


def triplet(nums):
    if len(nums) == 3 and (nums[0] + nums[1] + nums[2] == 0):
        return [nums]
    result = []
    nums.sort()

    right_index = len(nums) - 1
    for index, value in enumerate(nums):
        if value >= 0:
            break

        left_index = index + 1

        while right_index > left_index:
            left_value = nums[left_index]
            right_value = nums[right_index]

            # print(f"assert:{value}:{left_value}:{right_value}")
            if value + left_value + right_value == 0:
                result.append([value, left_value, right_value])
            right_index -= 1
        right_index = len(nums) - 1

    return result


@pytest.mark.parametrize(
    "nums,expected",
    [
        (
            [-1, 0, 1, 2, -1, -4],
            [[-1, -1, 2], [-1, 0, 1]],
        ),
        (
            [0, 1, 1],
            [],
        ),
    ],
)
def test_triplet(
    nums,
    expected,
):

    result = triplet(
        nums=nums,
    )

    assert result == expected
