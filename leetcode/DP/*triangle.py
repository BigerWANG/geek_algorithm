# coding: utf-8

"""
120. 三角形最小路径和

给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

 

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

 
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        dp = triangle
        for i in range(len(triangle)-2, -1, -1):  # 自底向上进行递推
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i+1][j+1], dp[i+1][j])
        return dp[0][0]


class Solution(object):
    def minimumTotal(self, triangle):
        """
        """
        if not triangle:
            return 0
        n = len(triangle)
        f = [[0] * n for _ in range(n)]
        f[0][0] = triangle[0][0]
        for i in range(1, n):
            f[i][0] = f[i-1][0] + triangle[i][0]  # 当j=0的时候，dp方程中的dp[i-1][j-1]是不对的，所以这里需要提前为f[i][0]赋值
            for j in range(1, i):
                f[i][j] = min(f[i-1][j], f[i-1][j-1]) + triangle[i][j]
            # 当在i行的最左侧时， 我们只能从第i-1行的最左侧移动过来。当i==j 时，f[i-1][j] 没有意义，因此状态转移方程如下
            f[i][i] = f[i-1][i-1] + triangle[i][i]
        return min(f[n-1])

t = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]


print Solution().minimumTotal(t)

