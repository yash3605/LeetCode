class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hs = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in hs:
                hs[nums[i]] = 1
            else:
                hs[nums[i]] += 1

            if hs[nums[i]] > n // 2:
                return nums[i]
        return 0

solution = Solution()
print(solution.majorityElement([2,2,1,1,1,2,2]))
print(solution.majorityElement([3, 2, 3]))
