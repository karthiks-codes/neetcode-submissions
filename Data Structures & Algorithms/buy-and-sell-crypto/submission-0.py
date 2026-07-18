class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max = 0
        for i in range(n):
            for j in range(i+1, n):
                if max < (prices[j] - prices[i]):
                    max = prices[j] - prices[i]

        return max
        