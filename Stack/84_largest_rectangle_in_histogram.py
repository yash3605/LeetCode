class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea

solution = Solution()
print(solution.largestRectangleArea([7,1,7,2,2,4]))
print(solution.largestRectangleArea([1,3,7]))
print(solution.largestRectangleArea([2,1,5,6,2,3]))
print(solution.largestRectangleArea([2,4]))
