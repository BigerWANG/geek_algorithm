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
递归公式： f(n, m) = (f(n-1, m) + m ) % n
"""



class Solution(object):
    def lastRemaining(self, n, m):
        l = range(n)
        index = self.f(n, m)
        return l[index]

    def f(self, n, m):
        if n <= 1:
            return 0
        return (self.f(n - 1, m) + m) % n


def test():
    n = 10
    m = 17
    print Solution().lastRemaining(n, m)


if __name__ == '__main__':
    test()
