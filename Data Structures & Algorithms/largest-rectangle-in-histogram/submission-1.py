class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # O(n) time and O(n) space
        # monotonic increasing stack, so whenever there is a smaller one, you pop all in the stack until condition is not met. 
        # so the width would be from the index you pop all the way until the stack is not popped
        # this is because you tryna find the max width with the max height
        # stack (height, start_pos)
        # area = height[i] * (j - i)
        stack = []
        res = 0
        n = len(heights)

        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][0] > height:
                h, i = stack.pop()
                area = h * (idx - i)
                res = max(area, res)
                start = i
                
            
            stack.append((height, start))
        # we need to handle the leftover bars which can be seen from case 1
        if stack:
            for hi, idx in stack:
                res = max(res, hi * (n - idx))       

        return res