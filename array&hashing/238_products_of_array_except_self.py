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
