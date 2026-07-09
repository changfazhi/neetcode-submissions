"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # i would say use normal graph dfs
        # instead of using visited, you can use a hashmap that acts as a adjacency list
        if not node:
            return None
        clone = {} # {old_node: new_node}

        def dfs(curr_node):
            # base case is that i am trying to clone something that i have already clone
            if curr_node in clone:
                return clone[curr_node]
            
            # else need to clone it and add to clone, nieghbour later
            copy = Node(curr_node.val)
            clone[curr_node] = copy

            # copy over all the old node neighbours to the new one
            for neigh in curr_node.neighbors:
                copy.neighbors.append(dfs(neigh))

            return copy

        
        return dfs(node)
        
