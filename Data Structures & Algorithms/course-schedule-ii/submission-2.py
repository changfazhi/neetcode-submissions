class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # TOPO SORT


        indegree = [0] * numCourses
        graph = defaultdict(list)

        # build the adjacancy list as well as the indegree
        for dst, src in prerequisites:
            graph[src].append(dst)
            indegree[dst] += 1
        
        
        # make the q and add all the indegree that is 0
        # while q, pop the q and append to a list
        # then explore its neighbour, minus the indegree so uk it can go to this course next
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []

        while q:
            val = q.popleft()
            res.append(val)

            for neighbour in graph[val]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        return [] if len(res) != numCourses else res
        
