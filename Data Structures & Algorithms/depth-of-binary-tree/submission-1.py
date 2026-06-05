# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # depth = dfs
        # whatever current node i am at it depends on my children in order to find the max depth
        # base case
        if not root:
            return 0 # it means i have hit the leaf node, and there is no more to add
        
        # subtrees
        leftTree = self.maxDepth(root.left)
        rightTree = self.maxDepth(root.right)

        # at each recursive call, i need to be finding the max depth so far then add 1 more for the current node that i am at
        return max(leftTree, rightTree) + 1