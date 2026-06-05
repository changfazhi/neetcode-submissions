# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            # base case 1: hit the leaf
            if not node:
                return None # since i need to return a node
            
            # base case 2: if p or q is a node, we need to return the node
            if (node and p and node.val == p.val) or (node and q and node.val == q.val):
                return node
            
            # subtrees 
            right = dfs(node.right)
            left = dfs(node.left)

            # because of base case 2 which only returns the node if it is equal to p or q, if both of them return a node it means both my children is p and q and thus i can return the node
            if left and right: # left and right contain node
                return node
            
            # there is no point in returning none, if both is none, none will be returned, however if one of them have a node we should traverse in that direction in order to look for the parent
            return left if left else right
        
        return dfs(root)