# coding: utf-8

"""
圆圈中最后剩下的数字
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

示例 1：

输入: n = 5, m = 3
输出: 3
示例 2：

输入: n = 10, m = 17
输出: 2

提示： 约瑟夫环
地推公式： f(n, m) = (f(n-1, m) + m ) % n
"""

# TODO: 约瑟夫环不懂


class Solution(object):
    # def lastRemaining(self, n, m):
    #     """
    #     :type n: int
    #     :type m: int
    #     :rtype: int
    #     """
    #     if not n:
    #         return None
    #     count = 0
    #     cycle_n = range(n)
    #     pop_value = []
    #     while len(cycle_n) > m:
    #         count += 1
    #         if count == m:
    #             cycle_n.pop()

    def lastRemaining(self, n, m):
        if n == 0:
            return 0









def test():
    n = 10
    m = 17
    a = Solution().lastRemaining(n, m)
    print a % n


if __name__ == '__main__':
    test()
