# coding: utf-8


"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""

from functools import reduce

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


class Solution1(object):
    def letterCombinations(self, digits):
        """
        变态解法，抄的
        :type digits: str
        :rtype: List[str]
        """

        def tool(l):
            return reduce(lambda a, b: [i+j for i in a for j in b], l)
        if not digits:
            return []
        nums = [KEYBOARD[num] for num in digits]
        return tool(nums)



class Solution(object):
    def letterCombinations(self, digits):
        """
        回溯算法
        :type digits: str
        :rtype: List[str]
        """
        res = []
        letters = []

        def backtrack(index):
            if index == len(digits):
                res.append(letters[:])
                return
            digit = digits[index]
            for i in KEYBOARD[digit]:
                letters.append(i)
                backtrack(index+1)
                letters.pop()

        backtrack(0)
        return ["".join(i) for i in res] if res else []


class Solution3(object):
    def letterCombinations(self, digits):
        """
        官方回溯解法
        :param digits:
        :return:
        """
        if not digits:
            return []
        def backtrack(index):
            if index == len(digits):
                res.append("".join(combin))
            else:
                digit = digits[index]
                for letter in KEYBOARD[digit]:
                    combin.append(letter)
                    backtrack(index+1)
                    combin.pop()
        res = []
        combin = []
        backtrack(0)
        return res







def test():
    res3 = Solution3().letterCombinations("23")
    print(res3)
    res2 = Solution2().letterCombinations("23")
    print(res2)



if __name__ == '__main__':
    test()
