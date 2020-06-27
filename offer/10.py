#coding: utf-8

"""
斐波那契数列
写一个函数，输入n 求斐波那契数列的底n 项
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
"""

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
        	return 0
        if n == 1:
        	return 1
        return 