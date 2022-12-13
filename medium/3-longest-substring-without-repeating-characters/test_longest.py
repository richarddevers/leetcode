import typing as t

import longest
import pytest


@pytest.mark.parametrize(
    "input,expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ],
)
def test_longest_substring(
    input: str,
    expected: int,
):
    result = longest.substring(input)

    assert result == expected
