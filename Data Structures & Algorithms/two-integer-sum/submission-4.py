class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        n = len(nums)
        # need to solve in O(n) time and space complexity
        for i in range(n):
            diff = target - nums[i]
            
            if nums[i] in comp and i != comp[nums[i]]:
                return [comp[nums[i]], i]
            else:
                comp[diff] = i
        
            
            