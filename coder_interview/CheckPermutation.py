# coding: utf-8

"""
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：

输入: s1 = "abc", s2 = "bca"
输出: true
示例 2：

输入: s1 = "abc", s2 = "bad"
输出: false

"""


class Solution(object):
    def CheckPermutation(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        排序再比较
        """
        return sorted(s1) == sorted(s2)


def test():
    s1 = "abc"
    s2 = "abd"
    Solution().CheckPermutation(s1, s2)


if __name__ == '__main__':
    test()
