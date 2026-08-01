"""
LeetCode #121: Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Constraints:
1 <= prices.length <= 10^5, 0 <= prices[i] <= 10^4
"""
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
