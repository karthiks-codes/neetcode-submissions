class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxP = 0

        for i in prices:
            if minPrice >= i:
                minPrice = i
            maxP = max(i - minPrice,maxP)

        return maxP
        
        