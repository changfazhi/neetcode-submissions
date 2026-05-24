class Solution:
    def rob(self, nums: List[int]) -> int:
        # O(n) space and time
        memo = [-1] * len(nums)
        
        def dfs(i):
            # in case i exceed 
            if i >= len(nums):
                return 0

            # return result of stored function calls ()
            
            if memo[i] != -1:
                return memo[i]

            # money at first


            money = max(nums[i] + dfs(i+2), dfs(i+1))
            # find highest money then rob next house
            
            
            memo[i] = money
            return memo[i]

        return dfs(0)