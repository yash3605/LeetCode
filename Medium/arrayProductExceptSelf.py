'''
    n = len(nums)
    res = [0] * n

    for i in range(n):
        product = 1
        for j in range(n):
            if i == j:
                continue
            product *= nums[j]
        res[i] = product
    return res
'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            print(prefix)
        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            print(postfix)
        return res
