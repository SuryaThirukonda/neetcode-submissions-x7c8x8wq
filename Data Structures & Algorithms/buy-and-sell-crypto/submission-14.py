class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        
        l =0 

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
                
            best = max(best, prices[r] -prices[l])

        return best
