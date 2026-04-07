class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        ind = 0
        for i in nums:
            comp = target - i
            if i in map1:
                return [map1[i], ind]
            else:
                map1[comp]=ind
            ind+=1

        