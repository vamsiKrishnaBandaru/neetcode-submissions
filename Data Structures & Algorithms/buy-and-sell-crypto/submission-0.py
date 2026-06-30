class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small, profit = prices[0], 0
        for price in prices:
            if small > price:
                small = price
            profit = max(profit, price - small)
        return profit