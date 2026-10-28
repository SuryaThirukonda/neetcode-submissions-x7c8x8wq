class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        t = set()
        l = 0
        for i in range(len(nums)):
            

            if abs(l-i) >k:
                t.remove(nums[l]) 
                l+=1

            curr = nums[i]
            if curr in t:
                return True
            else:
                t.add(curr)
        
        return False