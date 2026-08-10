class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        # create a 2d dp filled with 0s
        dp = [[0 for _ in range(m + 1)] for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                # we need to check all combinations of letters in text 1 and text 2
                # if they match means we can increment the i,j 
                if text1[i-1] == text2[j-1]:
                    # the next best combination of i,j would be i-1 and j-1 which holds the longest CS so far
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
                else:
                    # if the letters do not match, then we need to ignore one
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]