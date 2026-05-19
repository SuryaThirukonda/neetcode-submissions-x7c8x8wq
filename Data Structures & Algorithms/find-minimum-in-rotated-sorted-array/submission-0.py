class Solution:
    def findMin(self, nums: List[int]) -> int:
        while nums[0] > nums[- 1]:
            nums.insert(0,nums[- 1])
            nums.pop(-1)
        return nums[0]