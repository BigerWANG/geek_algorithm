# coding: utf-8

"""

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。


"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        start = -1
        ret = ""
        if not x:
            return 0
        while abs(start) <= len(s):
            ret += s[start]
            start -= 1
        if ret.endswith("-"):
            ret = ret[-1] + ret[:len(ret)-1]
        if ret.startswith("0"):
            ret = ret.strip("0")
        ret = int(ret)
        if (ret <= -2147483648) or (ret >= 2147483647):
            return 0
        return ret







def test():
    num = 0
    print Solution().reverse(num)


if __name__ == '__main__':
    test()
