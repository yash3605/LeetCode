"""
LeetCode #238: Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.

Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
"""
class Solution:
    def productExceptSelfWFU(self, nums: list[int]) -> list[int]:
        n = len(nums)
        out = [1] * n
        prefArr = [1] * n
        suffArr = [1] * n
        for i in range(1, n):
            prefArr[i] = prefArr[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffArr[i] = suffArr[i + 1] * nums[i + 1]

        for i in range(n):
            out[i] = prefArr[i] * suffArr[i]
        return out


    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        mult = 1
        for i in range(n - 2, -1 ,-1):
            mult *= nums[i + 1]
            res[i] *= mult

        return res

soution = Solution()
print(soution.productExceptSelf([1, 2, 4, 6]))
print(soution.productExceptSelf([-1, 0, 1, 2, 3]))
