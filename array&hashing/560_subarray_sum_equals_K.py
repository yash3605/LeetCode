from collections import defaultdict


class Solution:
    def subarraySumBF(self, nums: list[int], k: int) -> int:
        totalSubArray = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    totalSubArray += 1
        return totalSubArray

    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix = {0: 1}
        sum = res = 0
        for num in nums:
            sum += num
            if (sum - k) in prefix:
                res += prefix[sum - k]
            prefix[sum] = prefix.get(sum, 0) + 1
        return res


solution = Solution()
print(solution.subarraySum([1, 1, 1], 2))
print(solution.subarraySum([1, 2, 3], 3))
print(solution.subarraySum([2, -1, 1, 2], 2))
print(solution.subarraySum([4, 4, 4, 4, 4, 4], 4))
