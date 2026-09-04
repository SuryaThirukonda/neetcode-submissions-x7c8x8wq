class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        b = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in b:
                return [b[num],i]
            else:
                b[target-num] = i
    
        return [0,0]

        