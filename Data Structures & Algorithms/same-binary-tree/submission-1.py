# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # normal dfs becasue my current node depends on my children 
        # becuz if children diff then it is false
        # what are some cases where the trees are not the same
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        # subtrees to find deeper layer and see if these 3 cases still hold up
        leftTree = self.isSameTree(p.left, q.left)
        rightTree = self.isSameTree(p.right, q.right)
    
        return leftTree and rightTree # return both cus and will return the first flasy value