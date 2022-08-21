# Problem statement
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(list(range(1, len(nums) + 1))) - set(nums))


if __name__ == "__main__":
    input_list = [[4, 3, 2, 7, 8, 2, 3, 1], [1, 1]]
    output_list = [[5, 6], [2]]
    failed_solutions = 0
    for i in range(len(input_list)):
        print(Solution().findDisappearedNumbers(input_list[i]))
        try:
            assert Solution().findDisappearedNumbers(input_list[i]) == output_list[i]
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
