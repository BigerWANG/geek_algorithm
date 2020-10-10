# coding: utf-8

"""
最长公共子序列
"""


def recus_longest_common_subsecquence(s1, s2):
    """
    循环解法
    状态转义方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
    :param s1:
    :param s2:
    :return:
    """
    def dp(i, j):

        # 空字符串的case base
        if i == -1 or j == -1:
            return 0

        if s1[i] == s2[j]:
            return dp(i-1, j-1) + 1
        else:
            return max(dp(i-1, j), dp(i, j-1))

    return dp(len(s1) - 1, len(s2) - 1)


def loop_longest_common_subsecquence(s1, s2):
    """
    循环方法解决
    :param s1:
    :param s2:
    :return:
    """

    # 先生成dp table
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    print dp

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1  # 当前表格上的数字等于它上一个表格上的数字 + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]





print recus_longest_common_subsecquence("babcde", "acze")
print loop_longest_common_subsecquence("babcde", "acze")