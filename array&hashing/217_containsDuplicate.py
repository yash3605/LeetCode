"""
LeetCode #217: Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True

# logic second
'''
res = {}

        for n in nums:
            if n in res:
                return True
            else:
                res[n] = 1
        return False
'''
