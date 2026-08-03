class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # since it is not a grid, need build adjacancy list
        graph = defaultdict(list)
        for src, dst, weight in times:
            graph[src].append((dst, weight))
        
        # build a hashmap, where everything is infinite so that we can let it match curr distances if found
        distances = {i: float('inf') for i in range(1, n+1)}
        distances[k] = 0

        # build a min-heap (weight, node)
        min_heap = [(0, k)]

        # compare neighbour and add to min-heap in order to find time for all the nodes
        while min_heap:
            curr_dist, curr_node = heapq.heappop(min_heap)
            if curr_dist > distances[curr_node]:
                continue
            
            for neighbour, weight in graph[curr_node]:
                new_dist = curr_dist + weight
                if new_dist < distances[neighbour]:
                    distances[neighbour] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbour))
        
        for i in range(1, n+1):
            if distances[i] == float('inf'):
                return -1
        
        return max(distances.values())
            
        