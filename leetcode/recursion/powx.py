# coding: utf-8

"""
50. Pow(x, n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        算法：
        利用分治法的思想x ** n  = (x ** n//2) * (x ** n//2)
        进行递归求解
        递归终止条件是n <= 0
        """
        def helper(x, n):
            if n <= 0:
                return 1.0
            half = helper(x, n // 2)
            if n % 2 == 0: # 如果是偶数次幂，直接两个数相乘
                return half * half
            else:  # 如果是奇数次幂，需要多乘一次x本身
                return half * half * x

        if n >= 0:
            return helper(x, n)
        else:
            return 1 / helper(x, abs(n))




print(Solution().myPow(2.00000, 10))

