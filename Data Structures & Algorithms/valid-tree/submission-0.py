class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # dfs down to see and at each level i need to check for cyclic detection in a undirected graph
        # make adj list that is undirected
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # check for base case (the edges must be n - 1)
        if len(edges) != n - 1:
            return False
        
        # visited to check cycle
        visited = set()
        # dfs down and at each level check for cyclic detection
        # since this is an undirected graph, we can check the neighbour and equate to its parents to skip, because this means that i am at the same edge
        def dfs(node, parent):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour == parent: # same edge means i am simply moving back and forth in the same edge, so i need to skip
                    continue
                
                if neighbour in visited: # this is a cycle
                    return False
                
                # i need to dfs down
                if not dfs(neighbour, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n 
                