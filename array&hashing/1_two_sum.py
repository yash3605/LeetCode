"""
LeetCode #1: Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hs = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hs:
                return [hs[diff], i]
            hs[nums[i]] = i
        return []

'''
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
'''
