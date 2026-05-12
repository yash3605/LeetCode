class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, total = 0, 0
        res = float("inf")

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if res == float("inf") else res


solution = Solution()
print(solution.minSubArrayLen(10, [2, 1, 5, 1, 5, 3]))
print(solution.minSubArrayLen(5, [1, 2, 1]))
print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(solution.minSubArrayLen(4, [1, 4, 4]))
print(solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
