# coding: utf-8

"""
左旋转字符串
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

"""


class Solution(object):
    @staticmethod
    def reverseLeftWords(s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        if not s or not n:
            return ""
        return s[n:] + s[:n]




def test():
    s = "abcdefg"
    n = 2
    print Solution.reverseLeftWords(s, n) == "cdefgab"



if __name__ == '__main__':
    test()
