# Problem statement
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]


# Solution from satyamsinha93 using xor


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        xor_list = []
        for num in nums:
            xor ^= num
            xor_list.append(xor)
        print(xor_list)
        return xor


if __name__ == "__main__":
    input_list = [[2, 2, 1], [4, 1, 2, 1, 2], [1], [1, 1, 2]]
    output_list = [1, 4, 1, 2]
    failed_solutions = 0
    for i in range(len(input_list)):
        print(Solution().singleNumber(input_list[i]))
        try:
            assert Solution().singleNumber(input_list[i]) == output_list[i]
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
