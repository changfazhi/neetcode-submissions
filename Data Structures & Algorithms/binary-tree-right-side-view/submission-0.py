# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # right left view -> using BFS
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            n = len(q)
            current_node = []
            for _ in range(n):
                node = q.popleft() # to get the right side, pop right
                current_node.append(node.val)
                
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                
            res.append(current_node)
        

        result = []
        for level in res:
            result.append(level[0])
        
        return result