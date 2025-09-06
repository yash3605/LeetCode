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
