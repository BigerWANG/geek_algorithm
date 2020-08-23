# coding: utf-8

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        d = {"(":")", "{":"}", "[":"]"}
        stack = []
        for i in s:
            if not stack or d.get(stack[-1]) != i:
                stack.append(i)
            else:
                stack.pop()
        return not stack





def test():
    a =  "{}[]()"
    s = Solution()
    print(s.isValid(a))


if __name__ == '__main__':
    test()








