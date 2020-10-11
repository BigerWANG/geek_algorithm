# coding: utf-8


"""
63. 不同路径 II

m * n 的格子中存在障碍


输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

"""


class Solution(object):
    @staticmethod
    def uniquePathsWithObstacles(obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        1，
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        """

        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        if obstacleGrid[0][0] == 1:  # 出来就是障碍物 直接返回
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]  # 不使用原数组保存状态

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:  # 如果这一行没有障碍物
                    if i == j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp)
        return dp[-1][-1]



class Solution1:
    @staticmethod
    def uniquePathsWithObstacles(obstacleGrid):
        """

        dp 状态： dp[i][j] = dp[i-1][j] + dp[i][-1]

        限制条件：
            第一行默认为1：如果有障碍 则后边的状态都为0
            第一列默认为1：如果有障碍 则后边的状态都为0
        """

        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
            if obstacleGrid[i][0] == 1:
                break

        for j in range(n):
            dp[0][j] = 1
            if obstacleGrid[0][j] == 1:
                break

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i > 0 and j > 0:  # dp[i][j] 的其中一个点不在左边界或者上边界的时候 此时公式才生效
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

# d = [
#   [0, 0, 0, 1, 0, 0],
#   [0, 0, 0, 0, 0, 0],
#   [0, 0, 1, 0, 0, 0],
#   [0, 0, 1, 0, 0, 0],
# ]

# d = [[0]]
# d = [[1]]
d = [[0,0],[1,1],[0,0]]
# #

# 怎么知道应该开几个维度的dp数组：

print(Solution1.uniquePathsWithObstacles(d))
print("\n")
print(Solution.uniquePathsWithObstacles(d))