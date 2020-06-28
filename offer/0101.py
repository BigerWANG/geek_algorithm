# coding: utf-8

"""
判断字符串是否唯一
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：

输入: s = "leetcode"
输出: false
示例 2：

输入: s = "abc"
输出: true
限制：

0 <= len(s) <= 100
如果你不使用额外的数据结构，会很加分。

"""


class Solution(object):
    def isUnique(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        index = 0
        while index+1 <= len(astr):
            curr_s = astr[index]
            for i in astr[index+1:]:
                if curr_s == i:
                    return False
            index += 1
        return True

    def isUniqueBySet(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        return not len(set(astr)) == len(astr)



def test():
    s = "code"
    print Solution().isUniqueBySet(s)


if __name__ == '__main__':
    test()