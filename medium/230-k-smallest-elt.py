# 230. Kth Smallest Element in a BST

# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# https://www.youtube.com/watch?v=5LUXSvjmGCw&ab_channel=NeetCode

# Given the root of a binary search tree, and an integer k,
#  return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Example1:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Example2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
import pytest


class TreeNode:
    def __init__(
        self,
        val=0,
        left=None,
        right=None,
    ):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root, k):
    results = []

    def dfs(root, side):
        if root.val not in results:
            if side:
                results.append(root.val)
            else:
                results.insert(0, root.val)

        if root.right:
            dfs(
                root=root.right,
                side=True,
            )
        if root.left:
            dfs(
                root=root.left,
                side=False,
            )

    dfs(
        root,
        side=None,
    )
    return results[k - 1]


@pytest.mark.parametrize(
    "root,k,expected",
    [
        (
            TreeNode(
                val=3,
                right=TreeNode(
                    val=4,
                ),
                left=TreeNode(
                    val=1,
                    right=TreeNode(
                        val=2,
                    ),
                ),
            ),
            1,
            1,
        ),
        (
            TreeNode(
                val=5,
                right=TreeNode(
                    val=6,
                ),
                left=TreeNode(
                    val=3,
                    right=TreeNode(
                        val=4,
                    ),
                    left=TreeNode(
                        val=2,
                        left=TreeNode(
                            val=1,
                        ),
                    ),
                ),
            ),
            3,
            3,
        ),
    ],
)
def test_kth_smallest(
    root: TreeNode,
    k: int,
    expected: int,
):
    result = kth_smallest(
        root=root,
        k=k,
    )

    assert result == expected
