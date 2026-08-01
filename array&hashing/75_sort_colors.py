"""
LeetCode #75: Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, then blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively. You must solve this problem without using the library's sort function.

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
"""
class Solution:
    def sortColorsCS(self, nums: list[int]) -> None:
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1

        i = 0
        for j in range(len(count)):
            for _ in range(count[j]):
                nums[i] = j

    def sortColors(self, nums: list[int]) -> None:
        left, right = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        while i <= right:
            if nums[i] == 0:
                swap(left, i)
                left += 1
            elif nums[i] == 2:
                swap(i, right)
                right -= 1
            i += 1

solution = Solution()
arr = [2,0,2,1,1,0]
solution.sortColors(arr)
print(arr)
