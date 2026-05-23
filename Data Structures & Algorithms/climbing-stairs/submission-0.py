class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        # O(n) space and time
        if n in self.memo:
            return self.memo[n]
        
        if n <= 0:
            return 0
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        res = self.climbStairs(n-1) + self.climbStairs(n-2)


        self.memo[n] = res
        return self.memo[n]
        
        