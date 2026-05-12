class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        window = []
        left = 0
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                window.pop()
                left = right
            if prices[left] <= prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)

            window.append(prices[right])

        return maxProfit


solution = Solution()
print(solution.maxProfit([10, 1, 5, 6, 7, 1]))
print(solution.maxProfit([10, 8, 7, 5, 2]))
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([7, 6, 4, 3, 1]))
print(solution.maxProfit([2, 1, 2, 1, 0, 1, 2]))
