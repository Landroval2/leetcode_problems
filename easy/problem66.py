# Problem statement
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_calls = 0
        if digits[-1] != 9:
            digits[-1] += 1
            print(digits)
            return digits
        elif len(digits) == 1:
            return [1, 0]
        else:
            num_calls += 1
            new_digits = self.plusOne(digits[:-1])
            zeros = [0] * num_calls
            new_digits.extend(zeros)
            return new_digits


if __name__ == "__main__":
    input_list = [[1, 2, 3], [4, 3, 2, 1], [9], [9, 9]]
    output_list = [[1, 2, 4], [4, 3, 2, 2], [1, 0], [1, 0, 0]]
    failed_solutions = 0
    for i in range(len(input_list)):
        try:
            assert Solution().plusOne(input_list[i]) == output_list[i]
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
