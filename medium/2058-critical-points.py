# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

# A critical point in a linked list is defined as either a local maxima or a local minima.
# A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.
# A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.
# Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
# Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

# eg1:
# Input: head = [3,1]
# Output: [-1,-1]
# Explanation: There are no critical points in [3,1].

# eg2:
# Input: head = [5,3,1,2,5,1,2]
# Output: [1,3]
# Explanation: There are three critical points:
# - [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
# - [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
# - [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
# The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
# The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.

import typing as t

import pytest

Head = t.List[int]


def is_local_minimum(
    before: int,
    value: int,
    after: int,
) -> bool:
    return value < before and value < after


def is_local_maximum(
    before: int,
    value: int,
    after: int,
) -> bool:
    return value > before and value > after


def points(
    head: Head,
) -> Head:
    if len(head) < 4:
        return [-1, -1]

    critical_points = []

    for index, value in enumerate(head):
        if index == 0 or index == len(head) - 1:
            continue
        before = head[index - 1]
        after = head[index + 1]
        local_mini = is_local_minimum(
            before=before,
            value=value,
            after=after,
        )
        local_max = is_local_maximum(
            before=before,
            value=value,
            after=after,
        )

        if local_mini or local_max:
            critical_points.append(index + 1)

    if not critical_points:
        return [-1, -1]

    critical_points.sort()
    min_distance = critical_points[-1] - critical_points[-2]
    max_distance = critical_points[-1] - critical_points[0]

    return [min_distance, max_distance]


@pytest.mark.parametrize(
    "head,expected",
    [
        ([3, 1], [-1, -1]),
        ([3, 1, 2], [-1, -1]),
        ([3, 1, 3, 2], [1, 1]),
        ([5, 3, 1, 2, 5, 1, 2], [1, 3]),
        ([1, 3, 2, 2, 3, 2, 2, 2, 7], [3, 3]),
    ],
)
def test_critical_points(
    head: t.List[int],
    expected: t.List[int],
):
    result = points(
        head=head,
    )

    assert result == expected
