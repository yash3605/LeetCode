class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        memo = [-1] * n

        def dfs(i):
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]

            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]
        return min(dfs(0), dfs(1))

solution = Solution()
print(solution.minCostClimbingStairs([1,2,3]))
print(solution.minCostClimbingStairs([1,2,1,2,1,1,1]))
print(solution.minCostClimbingStairs([10,15,20]))
print(solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
