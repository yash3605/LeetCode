"""
LeetCode #153: Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]. Find the minimum element in the array. You must write an algorithm that runs in O(log n) time.

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All integers of nums are unique.
"""
class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        l , r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r)//2   
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res 
