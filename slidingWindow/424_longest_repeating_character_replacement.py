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
