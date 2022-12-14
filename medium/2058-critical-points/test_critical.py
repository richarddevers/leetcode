import typing as t

import critical
import pytest


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
    result = critical.points(
        head=head,
    )

    assert result == expected
