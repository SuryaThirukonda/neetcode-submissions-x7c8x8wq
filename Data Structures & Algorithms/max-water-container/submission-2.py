class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        front = 0
        end = n-1
        max1 = -1
        while (front<end):
           
            left = heights[front]
            right = heights[end]
            height = min(left,right)
            area = height*(end-front)
            if (area>max1):
                max1 = area
            if (left>right):
                end-=1
            elif (right>left):
                front+=1
            else:
                end-=1
            
        return max1
            
