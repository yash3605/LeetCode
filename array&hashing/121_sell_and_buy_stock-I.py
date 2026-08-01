"""
LeetCode #121: Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        minCost = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < minCost:
                minCost = prices[i]

            if prices[i] - minCost > profit:
                profit = prices[i] - minCost
        return profit
