class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in map1:
                return [map1[comp], i]
            map1[nums[i]] = i
        