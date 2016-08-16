# 这题竟然是DP, 其实是被惯性思维误导了, 如果仔细想想, 确实应该是DP

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for i in range(n + 1)]
        self.DP(dp, 1, n)
        return dp[1][n]
        
    def DP(self, dp, i, j): # 表示i到j, 在最坏的情况下, 我们需要付钱最少是多少.
        if i >= j:
            return 0
        if dp[i][j] != 0:
            return dp[i][j]
        else:
            ans = 2200000000
            for k in range(i, j + 1):
                ans = min(ans, k + max(self.DP(dp, i, k - 1), self.DP(dp, k + 1, j)))
            dp[i][j] = ans
            return ans
