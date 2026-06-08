# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        def dfs(node, max_so_far):
            if not node:
                return None
            
            if node.val >= max_so_far:
                count[0] += 1
            
            new_max = max(max_so_far, node.val)

            leftNode = dfs(node.left, new_max)
            rightNode = dfs(node.right, new_max)

            return leftNode and rightNode
        
        dfs(root, root.val)
        return count[0]