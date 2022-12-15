# 54. Spiral Matrix

# https://leetcode.com/problems/spiral-matrix/

# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

import typing as t

import pytest

Matrix = t.List[t.List[int]]


def spiral(
    matrix: Matrix,
) -> t.List[int]:
    result = []
    top = 0
    bottom = len(matrix)
    left = 0
    right = len(matrix[0])

    while left < right and top < bottom:
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom):
            result.append(matrix[i][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break

        for i in range(right - 1, left - 1, -1):
            result.append(matrix[bottom - 1][i])
        bottom -= 1

        for i in range(bottom - 1, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

    return result


@pytest.mark.parametrize(
    "matrix,expected",
    [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        ),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
            [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8],
        ),
    ],
)
def test_spiral(
    matrix: Matrix,
    expected: t.List[int],
):

    result = spiral(
        matrix=matrix,
    )

    assert result == expected
