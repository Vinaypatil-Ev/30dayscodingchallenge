class Solution:
    def countWays(self,m):
        # math way
        # return m // 2 + 1

        #dp approach
        dp = [0] * (m + 1)
        dp[0] = dp[1] = 1
        for i in range(2, m + 1):
            dp[i] = 1 + dp[i - 2]
        return dp[m]
