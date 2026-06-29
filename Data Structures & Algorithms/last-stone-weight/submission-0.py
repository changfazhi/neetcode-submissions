class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # n log n time and n space
        min_heap = []
        # i need to push all the stone to max_heap since we are interested in the heaviest stone
        # i need to pop the 2 heavist stone and go thru the if else clause
        # after that i need to push them back to the heap
        # dont stop until len(min_heap) <= 1
        for stone in stones:
            heapq.heappush(min_heap, -stone)
        
        while len(min_heap) > 1:
            # take out 2 heaviest stone
            x = -heapq.heappop(min_heap)
            y = -heapq.heappop(min_heap)

            # run thru the if else clause
            if x < y:
                heapq.heappush(min_heap, -(y-x))
            elif y < x:
                heapq.heappush(min_heap, -(x-y))
        
        return 0 if len(min_heap) == 0 else -min_heap[0]
            


        