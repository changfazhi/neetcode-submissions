class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # given that there is prerequisities -> most likely is to use topo sort
        indegree = [0] * numCourses
        graph = defaultdict(list)

        # make the adjancency list as well as collate the indegree
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1
        
        order = []
        # add to the q if the indegree is 0
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        # bfs ordering
        while q:
            course = q.popleft()
            order.append(course)

            for neighbour in graph[course]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        
        return len(order) == numCourses




