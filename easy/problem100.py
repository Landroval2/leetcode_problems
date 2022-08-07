# Problem statement
#
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            if p == q:
                return True
            else:
                return False

        self.isSameTree(p.right, q.right)
        return (
            (p.val == q.val)
            & (self.isSameTree(p.left, q.left))
            & (self.isSameTree(p.right, q.right))
        )


if __name__ == "__main__":
    input_Tree = [
        [TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))],
        [TreeNode(1, TreeNode(2)), TreeNode(1, TreeNode(None), TreeNode(2))],
        [TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2))],
        [TreeNode(None), TreeNode(None)],
        [TreeNode(), TreeNode(None)],
    ]
    output_Tree = [True, False, False, True, False]
    failed_solutions = 0
    for i in range(len(input_Tree)):
        print(Solution().isSameTree(input_Tree[i][0], input_Tree[i][1]))
        try:
            assert (
                Solution().isSameTree(input_Tree[i][0], input_Tree[i][1])
                == output_Tree[i]
            )
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
