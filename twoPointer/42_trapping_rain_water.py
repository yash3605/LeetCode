class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])


        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res



solution = Solution()
print(solution.trap([0,2,0,3,1,0,1,3,2,1]))
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(solution.trap([4,2,0,3,2,5]))
