# coding: utf-8

"""

面试题 01.06. 字符串压缩
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）

示例1:

 输入："aabcccccaaa"
 输出："a2b1c5a3"
示例2:

 输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。

"""


class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        start = 0   # 定义起始指针
        n_step = 0  # 下一个
        count = 0  # 计数器
        s = ""
        while True:
            _st = S[start]
            if n_step == len(S):  # 如果下一步长度等于字符串长度 说明已经到了末尾，把末尾的添加进去即可
                s += "{}{}".format(_st, count)
                break
            _next = S[n_step]
            if _st == _next:
                n_step += 1
                count += 1
            else:
                start = n_step
                n_step += 1
                s += "{}{}".format(_st, count)
                count = 1
        return s if len(s) < len(S) else S


def test():
    num = "xxxx"
    print Solution().compressString(num)


if __name__ == '__main__':
    test()
