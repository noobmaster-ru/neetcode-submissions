class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPriceBefore = prices[0]
        profit = 0
        for price in prices[1:]:
            if price - minPriceBefore > profit:
                profit = price - minPriceBefore
            if price < minPriceBefore:
                minPriceBefore = price
        return profit