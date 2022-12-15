import typing as t

import pytest

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


def are_anagram(
    s1: str,
    s2: str,
) -> bool:
    _s1 = list(s1)
    _s2 = list(s2)
    _s1.sort()
    _s2.sort()

    return _s1 == _s2


def group(
    inputs: t.List[str],
) -> t.List[t.List[str]]:
    i = 0
    result = []

    while i < len(inputs):
        remaining_list = inputs[i + 1 :]
        local_result = [inputs[i]]

        for elt in remaining_list:
            if are_anagram(
                s1=inputs[i],
                s2=elt,
            ):
                local_result.append(elt)
                local_result.sort()
                inputs.remove(elt)
        result.append(local_result)
        i += 1

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
