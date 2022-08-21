# Problem statement
# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

from sre_constants import RANGE_UNI_IGNORE
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum([self.nums[i] for i in range(left, right + 1)])


# Prayag777 solution


class NumArray:
    def __init__(self, nums: List[int]):
        self.sum_dict = {}
        sm = 0
        for i in range(len(nums)):
            sm += nums[i]
            self.sum_dict[i] = sm

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sum_dict[right]
        return self.sum_dict[right] - self.sum_dict[left - 1]


nums = NumArray([-2, 0, 3, -5, 2, -1])
print(nums.sumRange(2, 5))
