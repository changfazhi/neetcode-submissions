class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # O(n) time and O(1) space
        # need to have a variable max compare every iteration
        # need to have 2 pointers, first stay, second move
        p1 = 0
        p2 = 1
        n = len(heights)
        res = 0
        for j in range(n):
            for i in range(n-1):
                p2 = i + 1
                area = min(heights[p2], heights[p1]) * (p2 - p1)
                res = max(area, res)
            p1 += 1
            
        return res