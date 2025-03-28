class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = float("-inf")
        l = r = 0


        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                maxprofit = max(maxprofit, prices[r] - prices[l])
                r += 1
        
        return maxprofit
