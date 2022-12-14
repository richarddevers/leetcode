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
