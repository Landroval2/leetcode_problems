# Problem statement
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return 0
        if root.val == targetSum and (root.left is None and root.right is None):
            return 1
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
            root.right, targetSum - root.val
        )


if __name__ == "__main__":
    input_Tree = [
        [
            TreeNode(3, TreeNode(TreeNode(9)), TreeNode(20, TreeNode(15), TreeNode(7))),
            39,
        ],
        [
            TreeNode(
                1,
                TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
                TreeNode(2),
            ),
            0,
        ],
        [None, 0],
        [
            TreeNode(
                5,
                TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None),
                TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
            ),
            22,
        ],
        [TreeNode(1, TreeNode(2), TreeNode(3)), 5],
    ]
    output_Tree = [True, False, True, True, False]
    failed_solutions = 0
    for i in range(len(input_Tree)):
        print(Solution().hasPathSum(input_Tree[i][0], input_Tree[i][1]))
        try:
            assert (
                Solution().hasPathSum(input_Tree[i][0], input_Tree[i][1])
                == output_Tree[i]
            )
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
