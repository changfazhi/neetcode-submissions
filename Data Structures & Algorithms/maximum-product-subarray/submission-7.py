class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1
        for num in nums:
            temp = curMax * num # at the current iteration what is the num
            # change the curMax and curMin at the current iteration
            curMax = max(num, num * curMax, num * curMin)
            curMin = min(num, num * curMin, temp)
            res = max(res, curMax)
        
        return res
        