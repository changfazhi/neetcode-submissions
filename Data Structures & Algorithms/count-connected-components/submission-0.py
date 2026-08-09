class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # undirected graph -> i need to build adj list that is undirected as well

        # time/space is O(V + E)
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # i should dfs down and track visited
        # after dfs there are still not visited, then i will dfs those not visited
        # each dfs should increment my res
        res = 0
        visited = [False] * n
        
        # dfs helper function
        def dfs(node):
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    dfs(neighbour)
        
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                res += 1
        
        return res
