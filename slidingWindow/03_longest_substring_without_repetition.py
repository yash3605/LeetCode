class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        maxLen = 0

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen


solution = Solution()
print(solution.lengthOfLongestSubstring("zxyzxyz"))
print(solution.lengthOfLongestSubstring("xxxx"))
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("bbbbb"))
print(solution.lengthOfLongestSubstring("pwwkew"))
