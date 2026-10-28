class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        b = 0

        for s in range(len(prices)):
            if prices[s] < prices[b]:
                b=s

            best = max(best, prices[s] - prices[b])

        return best

            