# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # basically swapping left side of my children to right side and vice versa
        # so i am depending on my children thus i need to be using btm up dfs
        # base case is that my root is none
        if not root:
            return None
        
        # find my subtrees
        leftTree = self.invertTree(root.left)
        rightTree = self.invertTree(root.right)

        # swapping left to right
        root.left = rightTree
        root.right = leftTree

        return root