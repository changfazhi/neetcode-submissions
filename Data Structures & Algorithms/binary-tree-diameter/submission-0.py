# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            leftTree = dfs(root.left) # max depth of left tree
            rightTree = dfs(root.right) # max depth of right tree

            current_diamter = leftTree + rightTree
            res = max(res, current_diamter)

            return max(leftTree, rightTree) + 1
        
        dfs(root)
        return res

