# coding: utf-8


"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""

from functools import reduce

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        KEYBOARD = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def tool(l):
            return reduce(lambda a, b: [i+j for i in a for j in b], l)
        if not digits:
            return []
        nums = [KEYBOARD[num] for num in digits]
        return tool(nums)


def test():
    print(Solution().letterCombinations("235"))


if __name__ == '__main__':
    test()
