class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amt):
            if amt in memo:
                return memo[amt]
            
            if amt == 0:
                return 0

            res = 1092430981274892
            for coin in coins:
                if amt >= coin:
                    
                    res = min(res, dfs(amt - coin) + 1)
            
            memo[amt] = res
            return memo[amt]
        
        minCoins = dfs(amount)
        return -1 if minCoins >= 1092430981274892 else minCoins
