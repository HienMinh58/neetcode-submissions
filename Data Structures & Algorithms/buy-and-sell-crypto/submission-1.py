class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0
        while l <= len(prices) - 1:
            r = l + 1
            while r <= len(prices) - 1:
                maxP = max(maxP, (prices[r] - prices[l]))
                r += 1
            l += 1
        return maxP

