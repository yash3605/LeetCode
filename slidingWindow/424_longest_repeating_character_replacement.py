"""
LeetCode #424: Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character at most k times. Return the length of the longest substring containing the same letter you can get after performing the above operations.

Constraints:
1 <= s.length <= 10^5, s consists of only uppercase English letters, 0 <= k <= s.length
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hs = {}
        left = 0
        max_window = 0
        for right in range(len(s)):
            hs[s[right]] = 1 + hs.get(s[right], 0)

            window_len = right - left + 1
            max_f = max(hs.values()) if hs else 0

            if window_len - max_f > k:
                hs[s[left]] -= 1
                left += 1
            max_window = max(max_window, right - left + 1)

        return max_window


solution = Solution()
print(solution.characterReplacement("XYYX", 2))
print(solution.characterReplacement("AAABABB", 1))
print(solution.characterReplacement("ABAB", 2))
print(solution.characterReplacement("AABABBA", 1))
