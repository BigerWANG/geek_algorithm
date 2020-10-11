# coding: utf-8

"""
322. 零钱兑换

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。

 

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
示例 4：

输入：coins = [1], amount = 1
输出：1
示例 5：

输入：coins = [1], amount = 2
输出：2


提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 231 - 1
"""


def coin_change(coins, amount):
    """
    :param coins:
    :param amount:
    :return:
    """
    def dp(n):
        if n == 0:
            return 0
        if n < 0:
            return -1
    # 求最小值 所以初始化为正无穷
        res = float("INF")
        for coin in coins:
            sub = dp(n - coin)
            if sub == -1:
                continue
            res = min(res, sub+1)
        return res if res != float("INF") else -1

    return dp(amount)


def coin_change1(coins, amount):
    """
    自底向上
    :param coins:
    :param amount:
    :return:
    """
    dp = [amount + 1 for _ in range(amount + 1)]
    dp[0] = 0
    for i in range(len(dp)):
        for coin in coins:
            if i - coin < 0:
                continue
            dp[i] = min(dp[i], 1+dp[i-coin])
    return -1 if dp[amount] == amount + 1 else dp[amount]


def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    if not s: return -1
    from collections import Counter
    c = Counter(s)
    for i in range(len(s)):
        if c[s[i]] == 1:
            return i
    return -1


print firstUniqChar("addaddada")