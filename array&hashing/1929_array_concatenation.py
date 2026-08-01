"""
LeetCode #1929: Concatenation of Array

Given an integer array nums of length n, create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed). Return the array ans.

Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 1000
"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans
