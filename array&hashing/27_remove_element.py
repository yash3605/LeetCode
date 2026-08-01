"""
LeetCode #27: Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of elements may be changed. Then return the number of elements in nums which are not equal to val.

Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""
class Solution:
    def removeElements(self, nums: list[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1

        return j + 1
solution = Solution()
print(solution.removeElements([1,1,2,3,4], 1))
print(solution.removeElements([0,1,2,2,3,0,4,2], 2))
