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


def compute_word_key(
    word: str,
) -> str:
    count: t.List[str, int] = {}
    for char in word:
        count[char] = count.get(char, 0) + 1

    count_sorted = sorted(count.items(), key=lambda x: x[0])

    result = ""
    for elt in count_sorted:
        result += f"{elt[0]}{elt[1]}"
    return result


def group(
    inputs: t.List[str],
) -> t.List[t.List[str]]:
    result: t.List[t.List[str]] = []

    if len(inputs) <= 1:
        return [inputs]

    count = {}
    for word in inputs:
        key = compute_word_key(word)
        count[key] = count.get(key, []) + [word]

    for key, value in count.items():
        value.sort()
        result.append(value)
    result.sort()
    return result


@pytest.mark.parametrize(
    "inputs,expected",
    [
        (
            [""],
            [[""]],
        ),
        (
            ["a"],
            [["a"]],
        ),
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
