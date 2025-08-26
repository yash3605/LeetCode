class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hs = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hs:
                return [hs[diff], i]
            hs[nums[i]] = i
        return []

'''
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
'''
