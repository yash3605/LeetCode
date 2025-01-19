''' class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
         length = len(nums)

         for i in range(length):
            for j in range(i+1, length):
                if (nums[i] == nums[j]):
                    return True

         return False
'''


class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False

'''
  return True if len(set(nums)) < len(nums) else False
'''
