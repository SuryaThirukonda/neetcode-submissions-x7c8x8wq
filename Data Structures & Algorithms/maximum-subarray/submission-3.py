class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        l = 0
        best = -float("inf")
        for r in range(len(nums)):
            sum+=nums[r]

            best = max(best,sum)

            
            if sum <0:
                sum = 0
                l = r+1
        
        return best