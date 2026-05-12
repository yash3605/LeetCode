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
