# coding: utf-8


def feb(n):
    """
    斐波那契数列 DP 写法
    :param num:
    :return:
    """
    from collections import defaultdict
    d = defaultdict(int)
    if n <= 0:
        return 0
    d[0] = 0
    d[1] = 1
    for i in range(2, n+1):
        d[i] = d[i - 1] + d[i - 2]
    return d[n] % 1000000007


class Solution:
    def uniquePaths(self, m, n):
        # 先生成一个左右边界都为 1 的二维数组
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]








print(Solution().uniquePaths(4, 3))
