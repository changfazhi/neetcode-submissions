class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums # this is the lst of num
        

        

    def add(self, val: int) -> int:
        self.min_heap = []
        self.nums.append(val)
        for num in self.nums:
            heapq.heappush(self.min_heap, num)
        
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)
            
        return self.min_heap[0]
        
