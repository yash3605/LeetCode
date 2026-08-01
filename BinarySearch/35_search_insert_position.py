"""
LeetCode #35: Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order
-10^4 <= target <= 10^4
"""
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

            res = mid

        if nums[res]< target:
            return res + 1
        else:
            return res


solution = Solution()
print(solution.searchInsert([-1,0,2,4,6,8], 5))
print(solution.searchInsert([-1,0,2,4,6,8], 10))
print(solution.searchInsert([1,3,5,6], 5))
print(solution.searchInsert([1,3,5,6], 2))
print(solution.searchInsert([1,3,5,6], 7))
print(solution.searchInsert([1,3,5,6], 0))
print(solution.searchInsert([1, 3, 5, 7, 9], 6))
