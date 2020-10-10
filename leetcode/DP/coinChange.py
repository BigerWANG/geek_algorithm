# coding: utf-8


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        算法：
        凑成面值为11的最小数：
        1，凑成面值为10（11-1）的最小数 + 面值为1的硬币
        2，凑成面值为9（11-2）的最小数 + 面值为2的硬币
        3,凑成面值为6(11-5)的最小数 + 面值为5的硬币
        即 dp[11] = min (dp[11-1] + 1, dp[11-2] + 1, dp[11-5] + 1)。

        dp 方程
        dp[i] = min(dp[i], dp[i-coin] +1)
        """
        # 初始化值为正无穷，因为要判断最小
        # amount + 1是为了保证数据完整 （range 取值是0到n-1)
        dp = [float('INF') for _ in range(amount+1)]
        dp[0] = 0  # 初始化值一般是dp方程没办法计算出来的值
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1)
        return dp[amount] if dp[amount] != float('INF') else -1



def coin_change(coins, amount):
    """
    递归写法
    :param coins:
    :param amount:
    :return:
    """
    cache_dict = {}
    def recsion(coins, amount):
        res = float('INF')
        if not coins:
            return -1
        if amount == 0:
            return -1
        if cache_dict.get(amount):
            return cache_dict[amount]
        for i in coins:
            if amount >= i:
                res = min(recsion(coins, amount-i)+1, res)
                cache_dict[amount] = res
        return res if res != float('INF') else -1
    print(cache_dict)
    return recsion(coins, amount)


coins = [2,]
amount = 3
# print(coin_change(coins, amount))
print(Solution().coinChange(coins, 3))