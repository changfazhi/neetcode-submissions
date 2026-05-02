class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n) time and O(n) space
        # i need a variable that store the amount of water so far as it iterates
        # if found highest, next iteration need to find diff and add 
        # if found even higher, make it new highest
        # always diff with the highest found
        # keep adding until found height >= highest
        n = len(height)
        l, r = 0, n-1
        leftMax = height[l]
        rightMax = height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res