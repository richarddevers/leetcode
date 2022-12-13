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
