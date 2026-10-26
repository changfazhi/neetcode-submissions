class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        # i would need to use the 2 pointer approach
        left = 0
        right = n - 1
        
        # keep track of leftMax and rightMax
        leftMax = 0
        rightMax = 0

        # when pointer move, compare the max.
        while left < right:
            if heights[left] > leftMax:
                leftMax = heights[left]
            if heights[right] > rightMax:
                rightMax = heights[right]
            maxArea = (right - left) * min(leftMax, rightMax)
            res = max(maxArea, res)
        # which ever that is not max would move
            if leftMax > rightMax:
                right -= 1
            else:
                left += 1
        # at each iteration find the area and then compare with res and find the max area

        return res
        