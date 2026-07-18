class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i ^ num # i ^ num is to see if it will cancel out
            # if cancel out it would be 0 which would not change the res
            # if it doesnt cancel out it will change the res
            # res is set to be the length so that to asccount for the last number incase all match
        
        return res
        