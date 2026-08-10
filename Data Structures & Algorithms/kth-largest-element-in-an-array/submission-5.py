import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        i = 0
        for num in nums:
            heapq.heappush(pq,-1*num)
        
        while i<k-1:
            heapq.heappop(pq)
            i+=1
        
        return -heapq.heappop(pq)
