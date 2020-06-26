# coding: utf-8

"""

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return False

        return str(x) == str(x)[::-1]







def test():
    num = 123
    print Solution().isPalindrome(num)


if __name__ == '__main__':
    test()
