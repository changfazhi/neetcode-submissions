# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # need to use dfs and return its height or true / false -> so i need to use the third pattern
        def dfs(node):
            # base case
            if not node:
                return 0
            
            # recurse on the left and right sub trees
            leftTree = dfs(node.left)

            rightTree = dfs(node.right)

            # process 1 - if already checked that they are not balanced then jus return as it they are not balanced
            if leftTree == -1:
                return -1
            if rightTree == -1:
                return -1
            
            # process 2 - find the difference in heght
            diff = abs(leftTree - rightTree)
            if diff > 1:
                return -1
            
            # return the height of the subtree to the parent
            return max(leftTree, rightTree) + 1 # +1 is to include it self
        
        return dfs(root) != -1
