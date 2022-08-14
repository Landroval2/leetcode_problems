# Problem statement
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])

        return TreeNode(
            val=nums[len(nums) // 2],
            left=self.sortedArrayToBST(nums[: len(nums) // 2]),
            right=self.sortedArrayToBST(nums[(len(nums) // 2) + 1 :]),
        )


# TODO: FIX tests. There are several ways to define the trees. Find a way to print the solutions

if __name__ == "__main__":
    input_Tree = [[-10, -3, 0, 5, 9], [1, 3], []]
    output_Tree = [
        TreeNode(0, TreeNode(-3, TreeNode(-10)), TreeNode(9, TreeNode(5))),
        TreeNode(1, None, TreeNode(3)),
        None,
    ]
    failed_solutions = 0
    for i in range(len(input_Tree)):
        print(Solution().sortedArrayToBST(input_Tree[i]))
        try:
            assert Solution().sortedArrayToBST(input_Tree[i]) == output_Tree[i]
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
