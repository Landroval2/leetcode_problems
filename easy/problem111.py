# Problem statement
# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution from stevechk leetcode user


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        minDepth = float("inf")
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if node.left is None and node.right is None:
                minDepth = min(minDepth, depth)
            else:
                if node.left:
                    stack.append((node.left, depth + 1))
                if node.right:
                    stack.append((node.right, depth + 1))
        return minDepth


if __name__ == "__main__":
    input_Tree = [
        TreeNode(3, TreeNode(TreeNode(9)), TreeNode(20, TreeNode(15), TreeNode(7))),
        TreeNode(
            1,
            TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
            TreeNode(2),
        ),
        TreeNode(1, None, TreeNode(2, TreeNode(3, TreeNode(4)))),
        None,
        TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4)))),
        TreeNode(1, TreeNode(2), TreeNode(2)),
    ]
    output_Tree = [2, 2, 4, 0, 4, 2]
    failed_solutions = 0
    for i in range(len(input_Tree)):
        print(Solution().minDepth(input_Tree[i]))
        try:
            assert Solution().minDepth(input_Tree[i]) == output_Tree[i]
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
