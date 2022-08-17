# Problem statement
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)):
            if nums[i] != i:
                return i
        return len(nums)


if __name__ == "__main__":
    input_list = [[3, 0, 1], [0, 1], [9, 6, 4, 2, 3, 5, 7, 0, 1], [], [1], [0]]
    output_list = [2, 2, 8, 0, 0, 1]
    failed_solutions = 0
    for i in range(len(input_list)):
        try:
            assert Solution().missingNumber(input_list[i]) == output_list[i]
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
