# coding: utf-8

"""
一次编辑
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

 

示例 1:

输入:
first = "pale"
second = "ple"
输出: True
 

示例 2:

输入:
first = "pales"
second = "pal"
输出: False
"""


class Solution(object):
    def oneEditAway(self, first, second):
        """
        :type first: str
        :type second: str
        :rtype: bool
        """




def test():
    first = "pales"
    second = "pal"
    print Solution().oneEditAway(first, second)


if __name__ == '__main__':
    test()
