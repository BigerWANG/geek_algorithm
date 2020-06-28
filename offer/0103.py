# coding: utf-8

"""
URL化。编写一种方法，将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，
并且知道字符串的“真实”长度。

示例1:

 输入："Mr John Smith    ", 13
 输出："Mr%20John%20Smith"
示例2:

 输入："               ", 5
 输出："%20%20%20%20%20"



"""


class Solution(object):
    def replaceSpaces(self, S, length):
        """
        :type S: str
        :type length: int
        :rtype: str
        """
        return "%20".join(S[:length].split(" "))


def test():
    s1 = "nwmog q k  gW  c    H  DYpIE    Lcz         gV    Bj   vkH X g       l                                                                                        "
    length = 19
    print Solution().replaceSpaces(s1, length)


if __name__ == '__main__':
    test()
