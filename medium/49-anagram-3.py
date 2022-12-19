import typing as t

import pytest

# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]


def group(
    inputs: t.List[str],
) -> t.List[t.List[str]]:

    word_count = {}
    for word in inputs:
        char_count = [0] * 26
        for char in word:
            index = ord(char) - ord("a")
            char_count[index] += 1
        word_count[str(char_count)] = word_count.get(str(char_count), []) + [word]
    return sorted(list(word_count.values()))


@pytest.mark.parametrize(
    "inputs,expected",
    [
        # (
        #     [""],
        #     [[""]],
        # ),
        # (
        #     ["a"],
        #     [["a"]],
        # ),
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
    ],
)
def test_group(
    inputs: t.List[str],
    expected: t.List[t.List[str]],
) -> None:
    expected.sort()

    result = group(
        inputs=inputs,
    )

    assert result == expected
