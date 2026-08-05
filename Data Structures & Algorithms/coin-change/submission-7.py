class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 # there is 0 ways to get 0 amount
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], dp[a-c] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1