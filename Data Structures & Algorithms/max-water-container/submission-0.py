class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        front = 0
        end = n-1
        max1 = -1
        while (front<end):
            width = end-front
            left = heights[front]
            right = heights[end]
            height = min(left,right)
            area = height*width
            if (area>max1):
                max1 = area
            if (left>right):
                end-=1
            elif (right>left):
                front+=1
            else:
                front+=1
            
        return max1
            
