class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        

        def backtrack(can,total,ind):
            if (total==0):
                results.append(can.copy())
                return
            if total>0:
                for i in range(ind,len(nums)):
                    if (total-nums[i]<0):
                        continue
                    can.append(nums[i])
                    
                    backtrack(can,total-nums[i],i)

                    #remove for future backtracking
                    del can[-1]

        backtrack([],target,0)

        return results