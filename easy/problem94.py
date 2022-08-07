# Problem statement
# Given the root of a binary tree, return the inorder traversal of its nodes' values.


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.traversed_nodes = []

    # Recursive solution
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        self.inorderTraversal(root.left)
        self.traversed_nodes.append(root.val)
        self.inorderTraversal(root.right)
        return self.traversed_nodes

    # Iterative solution
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                self.traversed_nodes.append(curr.val)
                curr = curr.right
        return self.traversed_nodes


if __name__ == "__main__":
    input_Tree = [
        TreeNode(
            1,
            None,
            TreeNode(2, TreeNode(3), None),
        ),
        None,
        TreeNode(1),
    ]
    output_Tree = [[1, 3, 2], [], [1]]
    failed_solutions = 0
    for i in range(len(input_Tree)):
        print(Solution().inorderTraversal(input_Tree[i]))
        try:
            assert Solution().inorderTraversal(input_Tree[i]) == output_Tree[i]
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
