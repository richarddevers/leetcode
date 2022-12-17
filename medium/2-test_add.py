# https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

import typing as t

import add
import pytest


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),  # Explanation: 342 + 465 = 807.
        (
            [9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9],
            [8, 9, 9, 9, 0, 0, 0, 1],
        ),
    ],
)
def test_add_two_numbers(
    l1: t.List[int],
    l2: t.List[int],
    expected: t.List[int],
):
    result = add.two_numbers(
        l1=l1,
        l2=l2,
    )

    assert result == expected
