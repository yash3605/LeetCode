"""
LeetCode #704: Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.

Constraints:
1 <= nums.length <= 10^4
-10^4 < nums[i], target < 10^4
All integers of nums are unique
nums is sorted in ascending order.
"""
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (hi + lo) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1 
            else:
                hi = mid - 1
        return -1

solution = Solution()
print(solution.search([-1,0,2,4,6,8], 4))
print(solution.search([-1,0,2,4,6,8], 3))
print(solution.search([-1,0,3,5,9,12], 9))
print(solution.search([-1,0,3,5,9,12], 2))
