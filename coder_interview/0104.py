# coding: utf-8

"""
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。

 

示例1：

输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）

"""

from collections import Counter

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        每个字符出现的次数为偶数, 或者有且只有一个字符出现的次数为奇数时, 是回文的排列;
        否则不是.
        """
        c = Counter(s)
        values = c.values()
        res = map(lambda x: x % 2, values)
        res = [i for i in res if i > 0]  # 判断出现奇数次的字符的个数
        if len(res) > 1:  # 如果出现奇数次个数大于1 不是回文数
            return False
        return True




def test():
    s1 = "12123"
    print Solution().canPermutePalindrome(s1)


if __name__ == '__main__':
    test()
