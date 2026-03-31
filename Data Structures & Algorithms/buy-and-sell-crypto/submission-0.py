class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        L = 0
        R = 1

        while R < len(prices):
            if prices[L] < prices[R] :
                maxP = max(maxP, prices[R] - prices[L])
                
            else:
                L = R
            R = R + 1
        return maxP

        