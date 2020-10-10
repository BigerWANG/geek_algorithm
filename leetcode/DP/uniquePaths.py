# coding: utf-8





class Solution(object):
    @staticmethod
    def uniquePaths(m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        算法：
        dp表中每个格子都保存着从起始点到当前的步数
        1， 最小子问题: 假设只有两步可以走到target dp[m][n], 所以 dp[m][n] = dp[m-1][n] + dp[m][n-1]
        2, 状态转移方程： dp[i][j] = dp[i-1][j] + dp[i][j-1]
        3, 初始值和边界条件：
            1）因为只能往下走或者向右走，所以左边界和上边界的值都是1
            2）防止数组越界，循环起始点是1
        """
        if m == 0 or n == 0:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # 因为只能往下走或者向右走，所以左边界和上边界的值都是1
        dp[0] = [1 for _ in range(n)]
        for i in dp:
            i[0] = 1

        for i in range(1, m): # 从第一个网格开始走
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

res = Solution.uniquePaths(4, 3)
print(res)