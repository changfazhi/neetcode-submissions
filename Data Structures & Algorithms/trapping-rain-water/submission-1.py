class Solution:
    def trap(self, height: List[int]) -> int:
        # n time, n space
        res = 0
        n = len(height)
        # need to use 2 pointers in order to solve this problem
        left = 0
        right = n - 1
        # need to keep track of leftMax and rightMax
        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            # i need to compare the left and right max, the point is to find the tallest nigga, thats where you know you can trap the most water.
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                area = min(leftMax, rightMax) - height[left]
                if area > 0:
                    res += area
                
            # so whatever is lesser, you need to move it in order to find a taller tower
            # so at each iteration, you need to find the min of the maxes (as you can see from the first hole) x heigh[that you moved]
            # then you add the area. 
            # the idea is that, once you have a tall tower, whatever that is lower you add to the area just like 2 -> 0, 3 -> 1 -> 0 -> 1 -> 3
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                area = min(leftMax, rightMax) - height[right]
                if area > 0:
                    res += area
        
        return res
        