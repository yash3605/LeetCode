class Solution:
    def reverseString(self, s: list[str]) -> None:
        i, j = 0, len(s) - 1
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s


solution = Solution()
print(solution.reverseString(["h", "e", "l", "l", "o"]))
print(solution.reverseString(["H", "a", "n", "n", "a", "h"]))
print(solution.reverseString(["n", "e", "e", "t"]))
print(solution.reverseString(["r", "a", "c", "e", "c", "a", "r"]))
