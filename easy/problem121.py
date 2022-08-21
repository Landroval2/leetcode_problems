# Problem statement
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            if max_profit < prices[i] - lowest_price:
                max_profit = prices[i] - lowest_price
        return max_profit


if __name__ == "__main__":
    input_list = [[7, 1, 5, 3, 6, 4], [1, 1], [7, 6, 4, 3, 1]]
    output_list = [5, 0, 0]
    failed_solutions = 0
    for i in range(len(input_list)):
        print(Solution().maxProfit(input_list[i]))
        try:
            assert Solution().maxProfit(input_list[i]) == output_list[i]
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
