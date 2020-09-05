# coding: utf-8


"""
69
x 的平方根
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
"""

#
# class Solution(object):
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         平方根 就是存在整数a 满足 a**2 <= x <= (a + 1) **2
#         """
#         if x < 1: return 0
#
#         left, right = 1, x // 2 + 1
#
#         while left < right:
#             mid = (left + right + 1) // 2  # 这里取右中位数， 否则会造成死循环
#             square = mid * mid
#             if square > x:
#                 right = mid - 1
#             else:
#                 left = mid
#
#         return left

class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0

        left = 1
        right = x // 2
        while left < right:
            # 调试代码开始：为了仔细观察区间左右端点，我们每进入一次循环，让线程休眠 1 秒
            import time
            time.sleep(1)
            print('调试代码，观察区间左右端点、中位数，和进入的分支： left = {} , right = {} , '.format(left, right))
            # 调试代码结束

            # 错误代码，在分支左区间不发生收缩的情况下，中位数应该取右中位数
            # mid = left + (right - left) // 2
            mid = (left + right + 1) // 2
            # 调试代码
            print('mid = {} ,'.format(mid))
            square = mid * mid

            if square > x:
                # 调试代码
                print('进入 right = mid - 1 这个分支。')
                right = mid - 1
            else:
                # 调试代码
                print('进入 left = mid 这个分支。')
                left = mid
        return left



if __name__ == '__main__':
    print(Solution().mySqrt(9))
