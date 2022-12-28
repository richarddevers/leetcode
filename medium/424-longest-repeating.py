# 424. Longest Repeating Character Replacement

# https://leetcode.com/problems/longest-repeating-character-replacement/

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

import pytest

# def calcul_longest(
#     s1: str,
#     k: int,
# ) -> int:

#     longest = 1
#     left = 0
#     right = 1

#     while left < len(s1):
#         tmp = k
#         current_longest = 1
#         while right < len(s1):
#             # print(f"i:{left}, j:{right}")
#             if s1[left] != s1[right]:
#                 tmp -= 1
#             current_longest += 1
#             if current_longest > longest:
#                 longest = current_longest
#             if tmp == 0:
#                 break
#             right += 1

#         left += 1

#     return longest


# @pytest.mark.parametrize(
#     "s1,k,expected",
#     [
#         ("ABAB", 2, 4),
#         ("AABABBA", 1, 4),
#     ],
# )
# def test_calcul_longest(
#     s1,
#     k,
#     expected,
# ):

#     result = calcul_longest(
#         s1=s1,
#         k=k,
#     )

#     assert result == expected


def calcul_longest2(
    s1: str,
    k: int,
) -> int:
    compute_count = 0
    longest = 1
    left = 0

    def compute_slice(
        slice: str,
        longest,
        left: int,
        right: int,
    ) -> int:
        nonlocal compute_count
        compute_count += 1
        current_slide = slice[left:right]
        top_letter = current_slide.count(max(current_slide))
        to_change = len(current_slide) - top_letter
        print(f"top:{top_letter},slide:{current_slide}," f" tochange:{to_change}")
        if to_change <= k and longest < len(current_slide):
            longest = len(current_slide)
        return longest

    cache = []

    while left < len(s1) - 2:
        right = left + 2
        while right <= len(s1):
            if s1[left:right] not in cache:
                cache.append(s1[left:right])
                longest = compute_slice(
                    slice=s1,
                    longest=longest,
                    left=left,
                    right=right,
                )
            right += 1
        left += 1
    print(f"called:{compute_count}")
    return longest


@pytest.mark.parametrize(
    "s1,k,expected",
    [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
    ],
)
def test_calcul_longest2(
    s1,
    k,
    expected,
):

    result = calcul_longest2(
        s1=s1,
        k=k,
    )

    assert result == expected
