'''
def majorityElement(self, nums: list[int]) -> int:
    nums.sort()
    return nums[len(nums)//2]
'''

from collections import defaultdict

def majorityElement(self, nums: list[int]) -> int:
    count = defaultdict(int)
    res = maxCount = 0
    for num in nums:
        count[num] += 1
        if maxCount < count[num]:
            maxCount = count[num]
            res = num
    return res
