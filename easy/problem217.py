# Problem statement
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_list = nums.copy()
        new_list.sort()
        for i in range(len(nums) - 1):
            if (new_list[i] - new_list[i + 1]) == 0:
                return True
        return False


if __name__ == "__main__":
    input_list = [[1, 2, 3, 1], [1, 2, 3, 4], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], []]
    output_list = [True, False, True, False]
    failed_solutions = 0
    for i in range(len(input_list)):
        try:
            assert Solution().containsDuplicate(input_list[i]) == output_list[i]
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
