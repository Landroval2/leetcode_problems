# Problem statement
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        if m == 0:
            nums1[:] = nums2
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            else:
                nums1[i + j + 1] = nums2[j]
                j -= 1
        if i < 0:
            nums1[: j + 1] = nums2[: j + 1]
        else:
            nums1[: i + 1] = nums1[: i + 1]
        return nums1


# TODO: Change the tests
if __name__ == "__main__":
    input_list = [
        {"nums1": [1, 2, 3, 0, 0, 0], "m": 3, "nums2": [2, 5, 6], "n": 3},
        {"nums1": [1], "m": 1, "nums2": [], "n": 0},
        {"nums1": [0], "m": 0, "nums2": [1], "n": 1},
        {"nums1": [2, 0], "m": 1, "nums2": [1], "n": 1},
    ]
    output_list = [[1, 2, 2, 3, 5, 6], [1], [1], [1, 2]]
    failed_solutions = 0
    for i in range(len(input_list)):
        try:
            print(Solution().merge(**input_list[i]))
            assert Solution().merge(**input_list[i]) == output_list[i]
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
