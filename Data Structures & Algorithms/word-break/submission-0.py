class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # partition dp
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        #dp[i] means that from dp[0:i] it can be partitioned
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        
        return dp[-1]
        