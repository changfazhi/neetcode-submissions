class MedianFinder:

    def __init__(self):
        self.small = [] # max-heap
        self.large = [] # min-heap
        

    def addNum(self, num: int) -> None:
        # every number should be added to the small
        heapq.heappush(self.small, -num)
        # i need to ensure all small numbers are <= all large numbers
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # then i need to balance the length of the small and large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        # small at most 1 len bigger than large
        

    def findMedian(self) -> float:
        # if the total length is odd then just return small[0]
        # if it is even, need to small[0] + large[0] / 2
        n = len(self.small) + len(self.large)
        if n % 2 == 1:
            return float(-self.small[0])
        else:
            res = (-self.small[0] + self.large[0]) / 2
            return res
        
        
        