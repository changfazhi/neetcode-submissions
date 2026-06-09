# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float('-inf')]
        def dfs(node):
            if not node:
                return 0
            
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            curr_max = leftMax + rightMax + node.val
            max_sum[0] = max(max_sum[0], curr_max)

            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        return max_sum[0]
