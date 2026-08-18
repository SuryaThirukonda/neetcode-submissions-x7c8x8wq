class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tot = 0
        for num in nums:
            tot = tot ^ num
        return tot