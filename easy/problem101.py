# Problem statement
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.checkSymmetry(root.left, root.right)

    def checkSymmetry(
        self, left_node: Optional[TreeNode], right_node: Optional[TreeNode]
    ) -> bool:
        if left_node is None or right_node is None:
            return left_node == right_node
        if left_node.val != right_node.val:
            return False
        return self.checkSymmetry(
            left_node.left, right_node.right
        ) & self.checkSymmetry(left_node.right, right_node.left)


if __name__ == "__main__":
    input_Tree = [
        TreeNode(
            1,
            TreeNode(2, TreeNode(3), TreeNode(4)),
            TreeNode(2, TreeNode(4), TreeNode(3)),
        ),
        TreeNode(
            1,
            TreeNode(2, TreeNode(None), TreeNode(3)),
            TreeNode(1, TreeNode(2, TreeNode(None), TreeNode(3))),
        ),
        TreeNode(None),
        TreeNode(1, TreeNode(2)),
        TreeNode(1, TreeNode(2), TreeNode(2)),
    ]
    output_Tree = [True, False, True, False, True]
    failed_solutions = 0
    for i in range(len(input_Tree)):
        try:
            assert Solution().isSymmetric(input_Tree[i]) == output_Tree[i]
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
