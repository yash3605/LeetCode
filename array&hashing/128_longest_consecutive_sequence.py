class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hs = set(nums)
        longest = 0

        for num in hs:
            if num - 1 not in hs:
                length = 1
                while (num + length) in hs:
                    length += 1
                longest = max(length, longest)
        return longest


solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(solution.longestConsecutive([1, 0, 1, 2]))
