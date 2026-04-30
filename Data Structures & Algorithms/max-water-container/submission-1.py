class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # O(n) time and O(1) space
        # need to have a variable max compare every iteration
        # need to have 2 pointers, first stay, second move
        left = 0
        right = len(heights) - 1
        res = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            res = max(res, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return res