# 39. Combination Sum

# https://leetcode.com/problems/combination-sum/

# Given an array of distinct integers candidates and a target integer target,
#  return a list of all unique combinations of candidates where the chosen numbers sum to target.
#  You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target
#  is less than 150 combinations for the given input.

# Example1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example3:
# Input: candidates = [2], target = 1
# Output: []

import typing as t


def combination(
    candidates: t.List[int],
    target: int,
) -> t.List[t.List[int]]:
    res = []

    def dfs(
        i: int,
        cur: t.List[int],
    ):
        if i >= len(candidates) or sum(cur) > target:
            return

        if sum(cur) == target:
            res.append(cur.copy())
            return

        cur.append(candidates[i])
        dfs(i, cur)
        cur.pop()

        dfs(i + 1, cur)

    dfs(0, [])
    return res


def test_combination() -> None:
    candidates = [2, 3, 5]
    target = 8
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    # candidates = [2, 3, 6, 7]
    # target = 7
    # expected = [[2, 2, 3], [7]]

    result = combination(
        target=target,
        candidates=candidates,
    )

    assert result == expected
