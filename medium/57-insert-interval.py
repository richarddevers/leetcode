# <!-- 57. Insert Interval
# https://leetcode.com/problems/insert-interval/

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10]. -->

import typing as t

import pytest

Interval = t.List[t.List[int]]


def is_overlap(
    inter1: t.List[int],
    inter2: t.List[int],
) -> bool:
    return inter1[1] > inter2[0]


# [[1, 2], [3, 8], [8, 10], [12, 16]]
def insert(
    intervals: Interval,
    to_insert: t.List[int],
) -> Interval:
    res = []
    for index, value in enumerate(intervals):
        if to_insert[1] < value[0]:
            res.append(to_insert)
            return res + intervals[index:]
        elif to_insert[0] > value[1]:
            res.append(value)
        else:
            to_insert = [
                min(to_insert[0], value[0]),
                max(to_insert[1], value[1]),
            ]
    res.append(to_insert)
    return res


@pytest.mark.parametrize(
    "intervals,new_interval,expected",
    [
        (
            [[1, 3], [6, 9]],
            [-2, -1],
            [[-2, -1], [1, 3], [6, 9]],
        ),
        (
            [[1, 3], [6, 9]],
            [-1, 0],
            [[-1, 0], [1, 3], [6, 9]],
        ),
        (
            [[1, 3], [6, 9]],
            [11, 13],
            [[1, 3], [6, 9], [11, 13]],
        ),
        (
            [[1, 3], [9, 11]],
            [5, 7],
            [[1, 3], [5, 7], [9, 11]],
        ),
        (
            [[1, 3], [6, 9]],
            [2, 5],
            [[1, 5], [6, 9]],
        ),
        (
            [[1, 2], [3, 5]],
            [4, 8],
            [[1, 2], [3, 8]],
        ),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        ),
    ],
)
def test_insert(
    intervals: t.List[t.List[int]],
    new_interval: t.List[int],
    expected: t.List[t.List[int]],
) -> None:

    result = insert(
        intervals=intervals,
        to_insert=new_interval,
    )

    assert result == expected
