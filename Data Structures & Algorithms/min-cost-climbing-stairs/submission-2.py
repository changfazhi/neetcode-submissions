class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)
        def dfs(i):
            # if exceed the top floor
            if i >= len(cost):
                return 0

            # means it has been stored in my memo so i can use the stored result
            if memo[i] != -1:
                return memo[i]
            
            # the cost of floor 0 or 1 + min of taking 1 or 2 step
            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return memo[i]
        
        # see which one to take first, floor 0 or floor 1?
        return min(dfs(0), dfs(1))