import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = []

        for num in nums:
            heapq.heappush(self.pq,-num)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq,-val)

        temp = self.pq.copy()
        for i in range(self.k-1):
            heapq.heappop(temp)
        return -heapq.heappop(temp)

