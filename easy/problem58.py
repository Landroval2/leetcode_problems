# Problem statement
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split(" ")
        num_words = len(word_list)
        for i in range(num_words - 1, -1, -1):
            word_length = len(word_list[i])
            if word_length > 0:
                return word_length


# Better solution from user jsdsz. It iterates the list backwards until it finds a full word and returns its length.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        count = 0
        while i >= 0:
            if s[i] != " ":
                count += 1
                i -= 1
            elif count > 0 and s[i] == " ":
                break
            else:
                i -= 1
        return count


if __name__ == "__main__":
    input_list = [
        "Hello World",
        "   fly me   to   the moon  ",
        "luffy is still joyboy",
        "a",
        "a ",
    ]
    output_list = [5, 4, 6, 1, 1]
    failed_solutions = 0
    for i in range(len(input_list)):
        try:
            assert Solution().lengthOfLastWord(input_list[i]) == output_list[i]
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")
