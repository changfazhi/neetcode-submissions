# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0
        
        # need to use dfs duh
        leftTree = self.maxDepth(root.left)
        rightTree = self.maxDepth(root.right)

        # process - count the max number of nodes to hit the base case
        max_depth = max(leftTree, rightTree) + 1

        return max_depth


        