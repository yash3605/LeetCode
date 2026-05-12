class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                skipL = s[left + 1 : right + 1]
                skipR = s[left:right]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            left, right = left + 1, right - 1
        return True


solution = Solution()
print(solution.validPalindrome("aba"))
print(solution.validPalindrome("abca"))
print(solution.validPalindrome("abc"))
print(solution.validPalindrome("aca"))
print(solution.validPalindrome("abbadc"))
print(solution.validPalindrome("abbda"))
