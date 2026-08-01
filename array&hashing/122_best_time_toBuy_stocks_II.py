"""
LeetCode #122: Best Time to Buy and Sell Stock II

You are given an array prices where prices[i] is the price of a given stock on the ith day. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again). Return the maximum profit you can achieve.

Constraints:
1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
        return profit


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([1, 2, 3, 4, 5]))
print(solution.maxProfit([7, 6, 4, 3, 1]))
