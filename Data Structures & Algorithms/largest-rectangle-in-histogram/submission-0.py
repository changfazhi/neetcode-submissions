class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # find next smaller el from left using increasing mono stack
        stack = []
        left = [-1] * n
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        # find next smaller el from right using increasing mono stack
        stack = []
        right = [n] * n
        for i in range(n-1, -1, -1): # iterate backwards
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        # find largest area by r - l - 1 times height
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = width * heights[i]
            max_area = max(max_area, area)
        
        return max_area
