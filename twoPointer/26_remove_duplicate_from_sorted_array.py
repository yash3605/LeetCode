"""
LeetCode #26: Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. Return the number of unique elements in nums. The relative order of the elements should be kept the same.

Constraints:
1 <= nums.length <= 3 * 10^4, -100 <= nums[i] <= 100
"""
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique = 0
        for j in range(1, len(nums)):
            if nums[unique] != nums[j]:
                unique += 1
                nums[unique] = nums[j]
        return unique + 1


solution = Solution()
print(solution.removeDuplicates([1, 1, 2]))
print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(solution.removeDuplicates([1, 1, 2, 3, 4]))
print(solution.removeDuplicates([2, 10, 10, 30, 30, 30]))
