class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        ans=[]
        for i in range(len(nums)):
            if (nums[i]) in map1:
                ans = [map1[nums[i]], i]
                break
            else:
                map1[target-nums[i]] = i
        return ans