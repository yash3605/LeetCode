class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]

solution = Solution()
print(solution.rob([1,1,3,3]))
print(solution.rob([2,9,8,3,6]))
print(solution.rob([1,2,3,1]))
print(solution.rob([2,7,9,3,1]))
