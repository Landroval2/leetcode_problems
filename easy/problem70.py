# Problem statement
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    calculated_stairs = {}

    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        if n in self.calculated_stairs:
            return self.calculated_stairs[n]
        self.calculated_stairs[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.calculated_stairs[n]


if __name__ == "__main__":
    input_list = [1, 2, 3, 4]
    output_list = [1, 2, 3, 5]
    failed_solutions = 0
    for i in range(len(input_list)):
        try:
            assert Solution().climbStairs(input_list[i]) == output_list[i]
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
