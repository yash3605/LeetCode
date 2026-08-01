"""
LeetCode #344: Reverse String

Write a function that reverses a string. The input string is given as an array of characters s. You must do this by modifying the input array in-place with O(1) extra memory.

Constraints:
1 <= s.length <= 10^5, s[i] is a printable ascii character.
"""
class Solution:
    def reverseString(self, s: list[str]) -> None:
        i, j = 0, len(s) - 1
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


solution = Solution()
print(solution.reverseString(["h", "e", "l", "l", "o"]))
print(solution.reverseString(["H", "a", "n", "n", "a", "h"]))
print(solution.reverseString(["n", "e", "e", "t"]))
print(solution.reverseString(["r", "a", "c", "e", "c", "a", "r"]))
