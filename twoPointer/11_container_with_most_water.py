class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1       
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(area, res)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
        

solution = Solution()
print(solution.maxArea([1,7,2,5,4,7,3,6]))
print(solution.maxArea([2, 2, 2]))
print(solution.maxArea([1, 1]))
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
