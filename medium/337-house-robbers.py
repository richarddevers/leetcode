import typing as t

Root = t.List[int]


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


def dfs(
    root: TreeNode,
) -> t.Tuple[int, int]:  # (with_root, without_root)
    if not root:
        return (0, 0)

    if root.left:
        left_pair = dfs(root.left)
    else:
        left_pair = (0, 0)

    if root.right:
        right_pair = dfs(root.right)
    else:
        right_pair = (0, 0)

    with_root = root.val + left_pair[1] + right_pair[1]
    without_root = max(left_pair) + max(right_pair)

    return (with_root, without_root)


def rob(
    root: TreeNode,
) -> int:
    return max(
        dfs(
            root=root,
        )
    )


import house
import pytest

TreeNode = house.TreeNode

first_test = (
    TreeNode(
        val=3,
        left=TreeNode(
            val=2,
            left=None,
            right=TreeNode(
                val=3,
                left=None,
                right=None,
            ),
        ),
        right=TreeNode(
            val=3,
            left=None,
            right=TreeNode(
                val=1,
                left=None,
                right=None,
            ),
        ),
    ),
    7,
)

second_test = (
    TreeNode(
        val=3,
        left=TreeNode(
            val=4,
            left=TreeNode(
                val=1,
                left=None,
                right=None,
            ),
            right=TreeNode(
                val=3,
                left=None,
                right=None,
            ),
        ),
        right=TreeNode(
            val=5,
            left=None,
            right=TreeNode(
                val=1,
                left=None,
                right=None,
            ),
        ),
    ),
    9,
)


@pytest.mark.parametrize(
    "root,expected",
    [
        first_test,
        second_test,
    ],
)
def test_rob(
    root: TreeNode,
    expected: int,
):

    result = house.rob(
        root=root,
    )

    assert result == expected
