# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # find the longest path (max/min/count)
        # to return to my parent, i need to give my the max depth so far in order to find longest pathg
        # need to use global sum to track max length
        max_length = [0]
        # dfs down 
        def dfs(tree):
            # base case is that i hit a leaf - correct
            if not tree:
                return 0
            
            # find subtrees - correct
            leftTree = dfs(tree.left)
            rightTree = dfs(tree.right)

            # process and update the max length
            cur_length = leftTree + rightTree
            max_length[0] = max(cur_length, max_length[0]) # correct

            # return to my parent the max depth - correct
            return max(leftTree, rightTree) + 1
        
        dfs(root)
        return max_length[0]
