# 19. Remove Nth Node From End of List

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

import typing as t

import pytest

# def remove(
#     head: t.List[int],
#     n: int,
# ) -> t.List[int]:
#     head.pop(n + 1)
#     return head


# def test_remove():
#     head = [1, 2, 3, 4, 5]
#     n = 2
#     expected = [1, 2, 3, 5]

#     result = remove(
#         head=head,
#         n=n,
#     )

#     assert result == expected


# def remove2(
#     head: t.List[int],
#     n: int,
# ) -> t.List[int]:
#     return head[: n + 1] + head[n + 2 :]


# def test_remove2():
#     head = [1, 2, 3, 4, 5]
#     n = 2
#     expected = [1, 2, 3, 5]

#     result = remove2(
#         head=head,
#         n=n,
#     )

#     assert result == expected


# def remove3(
#     head: t.List[int],
#     n: int,
# ) -> t.List[int]:
#     res = []
#     for index, value in enumerate(head):
#         if index != n + 1:
#             res.append(value)
#     return res


# def test_remove3():
#     head = [1, 2, 3, 4, 5]
#     n = 2
#     expected = [1, 2, 3, 5]

#     result = remove3(
#         head=head,
#         n=n,
#     )

#     assert result == expected


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove4(
    head: ListNode,
    nn: int,
) -> ListNode:
    def dfs(
        i: int,
        nn: int,
        head: ListNode,
    ):
        if not head.next:
            return
        if i == nn:
            head.next = head.next.next

        dfs(
            i=i + 1,
            head=head.next,
            nn=nn,
        )

    dfs(
        i=0,
        head=head,
        nn=nn,
    )

    return head


def extract_linked_value(head: ListNode) -> t.List[int]:
    res = []

    def dfs(head: ListNode):
        res.append(head.val)
        if not head.next:
            return
        dfs(head=head.next)

    dfs(head=head)
    return res


def test_remove4():
    nn = 2
    head = ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(
                val=3,
                next=ListNode(
                    val=4,
                    next=ListNode(
                        val=5,
                    ),
                ),
            ),
        ),
    )
    expected = [1, 2, 3, 5]

    result = remove4(
        head=head,
        nn=nn,
    )

    assert extract_linked_value(result) == expected
