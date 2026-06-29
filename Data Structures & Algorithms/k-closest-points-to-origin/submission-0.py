class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # to find closest is like finding smallest, so i need to be using a max-heap
        max_heap = []

        # now i need to go thru all the points and find their distance and then add distance to the max_heap
        # then find the k shorest distance
        # then using the distance i need to find back the point
        # this means that i need to find the idx of the points first and map it
        for idx, point in enumerate(points):
            x = point[0]
            y = point[1]
            dist = ((x-0)**2 + (y-0)**2) ** 0.5
            heapq.heappush(max_heap, (-dist, idx))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        # now heap_max contain k shortest distance along with their idx
        res = []
        for item in max_heap:
            res.append(points[item[1]])
        
        return res
            


        