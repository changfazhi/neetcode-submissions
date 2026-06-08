# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # initalise lst and store all the nodes from smallest to largest. I will stop when the len of lst become k
        lst = []
        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)
            lst.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return lst[k-1]






        