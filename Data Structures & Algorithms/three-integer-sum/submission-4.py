class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        leng = len(nums)
        
        bob = []
        for i in range(leng-1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            fixed = nums[i]
            front = i+1
            end = leng-1

            while (front<end):
                if ( (fixed + nums[front] + nums[end]) == 0):
                    bob.append([fixed,nums[front], nums[end]])
                    end-=1
                    front+=1
                    while (front<end) and nums[front] == nums[front-1]:
                        front+=1
                    while (front<end) and nums[end]== nums[end+1]:
                        end-=1
                elif ((fixed + nums[front] + nums[end]) < 0):
                    front+=1
                elif ((fixed + nums[front] + nums[end]) > 0):
                    end-=1
                

        return bob
                

            