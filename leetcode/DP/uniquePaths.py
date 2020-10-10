# coding: utf-8


class Solution(object):
    @staticmethod
    def uniquePaths(m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        算法：
        1，生成一个m*n的网格，网格的左边界和右边界为1
        2，dp公式：dp[i][j] = dp[i+1][j]+dp[i][j+1]
        3, 返回最大值即 dp[i][j]
        """
        if m == 0 or n == 0:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # 因为只能往下走或者向右走，所以
        dp[0] = [1 for _ in range(n)]
        for i in dp:
            i[0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

res = Solution.uniquePaths(4, 3)
print(res)