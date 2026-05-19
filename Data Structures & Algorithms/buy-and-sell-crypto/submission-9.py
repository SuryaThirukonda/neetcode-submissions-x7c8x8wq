class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=0
        profit = 0

        if not prices or len(prices)==1:
            return 0
        
            
        for j in range(1,len(prices)):
            if (prices[j]< prices[b] ):
                b=j
            if (prices[j] - prices[b] > profit):
                profit = prices[j] - prices [b]
                
            
                
        return profit
            
