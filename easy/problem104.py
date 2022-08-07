# Problem statement
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    input_Tree = [
        TreeNode(3, TreeNode(TreeNode(9)), TreeNode(20, TreeNode(15), TreeNode(7))),
        TreeNode(1, TreeNode(None), TreeNode(2)),
        None,
        TreeNode(1, TreeNode(2)),
        TreeNode(1, TreeNode(2), TreeNode(2)),
    ]
    output_Tree = [3, 2, 0, 2, 2]
    failed_solutions = 0
    for i in range(len(input_Tree)):
        print(Solution().maxDepth(input_Tree[i]))
        try:
            assert Solution().maxDepth(input_Tree[i]) == output_Tree[i]
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
