# Problem statement
# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        start = 1
        end = x
        while start < end:
            mid = (start + end) // 2
            if start == mid or (mid * mid == x):
                return mid
            elif mid * mid > x:
                end = mid
            else:
                start = mid


if __name__ == "__main__":
    input_list = [4, 8, 0, 1]
    output_list = [2, 2, 0, 1]
    failed_solutions = 0
    for i in range(len(input_list)):
        try:
            assert Solution().mySqrt(input_list[i]) == output_list[i]
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
