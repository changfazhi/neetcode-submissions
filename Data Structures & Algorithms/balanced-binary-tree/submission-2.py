# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # track height -> abs(left, right) > 1 => not balanced => False
        # true or false
        # automatic template 3, require global value (true or false)
        # global values be height
        # can use -1 flag to end early
        def dfs(node):
            if not node:
                return 0
            
            # subtrees
            leftTree = dfs(node.left)
            rightTree = dfs(node.right)

            if leftTree == -1:
                return -1
            
            if rightTree == -1:
                return -1
            
            if abs(leftTree - rightTree) > 1:
                return -1
            
            return max(leftTree, rightTree) + 1
            
        
        return dfs(root) != -1


