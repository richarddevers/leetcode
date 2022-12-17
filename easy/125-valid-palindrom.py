# 125. Valid Palindrome

# https://leetcode.com/problems/valid-palindrome/

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

import typing as t

import pytest


def is_palindrom(
    s1: str,
) -> bool:
    s1_lowercase = s1.lower()
    s1_only_alphanumerical = [char for char in s1_lowercase if char.isalnum()]

    return s1_only_alphanumerical == s1_only_alphanumerical[::-1]


def is_palindrom2(
    s1: str,
) -> bool:
    s1_lowercase = s1.lower()
    s1_only_alphanumerical = [char for char in s1_lowercase if char.isalnum()]

    for i in range(len(s1_only_alphanumerical)):
        if s1_only_alphanumerical[i].lower() == s1_only_alphanumerical[-i - 1].lower():
            continue
        return False
    return True


def is_palindrom3(
    s1: str,
) -> bool:
    s1_lowercase = s1.lower()
    s1_only_alphanumerical = [char for char in s1_lowercase if is_alphanum(c=char)]

    for i in range(len(s1_only_alphanumerical)):
        if s1_only_alphanumerical[i].lower() == s1_only_alphanumerical[-i - 1].lower():
            continue
        return False
    return True


def is_alphanum(c: str) -> bool:
    return (
        ord("A") <= ord(c) <= ord("Z")
        or ord("a") <= ord(c) <= ord("z")
        or ord("0") <= ord(c) <= ord("9")
    )


@pytest.mark.parametrize(
    "s1,expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ],
)
def test_is_palindrom(
    s1: str,
    expected: bool,
) -> None:

    result = is_palindrom(
        s1=s1,
    )

    assert result == expected


@pytest.mark.parametrize(
    "s1,expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ],
)
def test_is_palindrom2(
    s1: str,
    expected: bool,
) -> None:

    result = is_palindrom(
        s1=s1,
    )

    assert result == expected


@pytest.mark.parametrize(
    "s1,expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ],
)
def test_is_palindrom3(
    s1: str,
    expected: bool,
) -> None:

    result = is_palindrom3(
        s1=s1,
    )

    assert result == expected
