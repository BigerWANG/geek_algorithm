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
        需要满足以下条件：
        1，如果长度相等：不相同的字符不能超过1个
        2，如果长度相差1，短的所有字符应该都在长的中
        3，否则返回False
        """
        if not first or not second:
            return False
        # 长度相同不同的字符串不能超过一个
        fl, sl = len(first), len(second)
        count = 0
        if fl == sl:
            pass
        elif (fl - sl) == 1:
            if len(first) > len(second):
                for i in second:
                    if i not in first:
                        return False
            else:
                for i in first:
                    if i not in second:
                        return False


def test():
    first = "palsss"
    second = "pallll"
    print Solution().oneEditAway(first, second)


if __name__ == '__main__':
    test()
