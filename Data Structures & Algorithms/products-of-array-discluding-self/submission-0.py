class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) for both space and time
        # requires one loop, should create prefix and suffix to store those results
        prefix = [] # [1,1,2,8]
        suffix = [] # [1,6,24,48] -> [48,24,6,1]
        res = []
        n = len(nums)
        
        length = 0
        for _ in range(n):
            prefixCount = 1
            suffixCount = 1
            for i in range(length):
                prefixCount *= nums[i]
            for j in range(n-1, length, -1):
                suffixCount *= nums[j]
            length += 1
            
            suffix.append(suffixCount)
            prefix.append(prefixCount)
        
        

        for k in range(n):
            resNum = (prefix[k] * suffix[k])
            res.append(resNum)

        return res