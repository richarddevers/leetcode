# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
#  typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false


def is_anagram(
    s1: str,
    s2: str,
) -> bool:
    if len(s1) != len(s2):
        return False
    return set(s1) == set(s2)


def is_anagram2(
    s1: str,
    s2: str,
) -> bool:
    if len(s1) != len(s2):
        return False

    count_s1 = {}
    count_s2 = {}

    for i in range(len(s1)):
        count_s1[s1[i]] = 1 + count_s1.get(s1[i], 0)
        count_s2[s2[i]] = 1 + count_s2.get(s2[i], 0)

    return count_s1 == count_s2


def test_is_anagram() -> None:
    s1 = "anagram"
    s2 = "nagaram"
    expected = True

    result = is_anagram2(
        s1=s1,
        s2=s2,
    )

    assert result == expected
