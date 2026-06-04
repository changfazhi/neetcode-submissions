# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # i should recurse down and at each level match them to see if they are equal
        # if equal i can return false else just keep going
        # if i reach base case means that i cannot find and i should return fakse

        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        # subtrees
        leftTree = self.isSubtree(root.left, subRoot)
        rightTree = self.isSubtree(root.right, subRoot)

        return leftTree or rightTree
    

    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        