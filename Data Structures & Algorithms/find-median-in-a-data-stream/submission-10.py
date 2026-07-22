import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        small = self.small
        large = self.large

        if not small:
            heapq.heappush(small,-1*num)
        else:
            if num>(-1*small[0]):
                heapq.heappush(large, num)
            else:
                heapq.heappush(small,-1*num)
            if abs(len(small)-len(large))>1:
                #equalize lengths
                if (len(small)>len(large)):
                    heapq.heappush(large,-1*heapq.heappop(small))
                else:
                    heapq.heappush(small, -1*heapq.heappop(large))
                    
        #if length is the same, then push the number to either larger or smaller elements
        #small is the smaller numbers, large is the larger numbers
        #small is a max heap, large is a min heap
        # if the heaps have different lengths, then we would do a heap push to the smaller one
    def findMedian(self) -> float:
        small = self.small
        large = self.large

        
        if (len(small)==len(large)):
            return float(-1*small[0]+large[0]) / 2
        else:
            if len(small)>len(large):
                return float(-1*small[0])
            else:
                return float(large[0])
        
        