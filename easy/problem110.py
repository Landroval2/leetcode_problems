# Problem statement
# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.lenTree(root) == 0:
            return True
        return (
            abs(self.lenTree(root.left) - self.lenTree(root.right)) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    def lenTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.lenTree(root.left), self.lenTree(root.right)) + 1


if __name__ == "__main__":
    input_Tree = [
        TreeNode(3, TreeNode(TreeNode(9)), TreeNode(20, TreeNode(15), TreeNode(7))),
        TreeNode(
            1,
            TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
            TreeNode(2),
        ),
        TreeNode(1, TreeNode(None), TreeNode(2, TreeNode(3, TreeNode(4)))),
        None,
        TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4)))),
        TreeNode(1, TreeNode(2), TreeNode(2)),
    ]
    output_Tree = [True, False, False, True, False, True]
    failed_solutions = 0
    for i in range(len(input_Tree)):
        print(Solution().isBalanced(input_Tree[i]))
        try:
            assert Solution().isBalanced(input_Tree[i]) == output_Tree[i]
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
