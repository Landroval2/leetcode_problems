# Problem statement
# Given two binary strings a and b, return their sum as a binary string.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = str(bin(int(a, 2) + int(b, 2)))[2:]
        return sum


if __name__ == "__main__":
    input_list = [["11", "1"], ["1010", "1011"], ["0", "0"]]
    output_list = ["100", "10101", "0"]
    failed_solutions = 0
    for i in range(len(input_list)):
        try:
            assert (
                Solution().addBinary(input_list[i][0], input_list[i][1])
                == output_list[i]
            )
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
