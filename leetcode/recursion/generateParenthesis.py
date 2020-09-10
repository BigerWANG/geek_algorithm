# coding: utf-8

"""
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。



示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 1:
            return ""


        res = []
        def generate(left, right, s, n):  # 左括号长度，右括号长度，
            # 终止条件
            if left == n and right == n:
                res.append(s)
                return
            if left < n:
                generate(left+1, right, s+"(", n)

            if right < left:
                generate(left, right+1, s+")", n)
        generate(0,0,"",n)
        return res



print(Solution().generateParenthesis(3))



