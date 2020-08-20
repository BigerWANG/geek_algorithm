# coding: utf-8

"""
根据每日 气温 列表，请重新生成一个列表，
对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
"""


class Solution(object):

    def dailyTemperatures(self, T):
        """
        维护一个递减栈，后入栈的元素总比栈顶元素小
        对比当前元素与栈顶元素的大小：
        1，当前元素 < 栈顶元素：入栈
        2，当前元素 > 栈顶元素：弹出栈顶元素，记录下两者下标即为所求天数
        * 用栈记录的是T的下标
        """
        stack = list()
        t_length = len(T)
        res_list = [0 for _ in range(t_length)]
        for key, value in enumerate(T):
            while stack and T[stack[-1]] < value:
                res_list[stack[-1]] = key - stack[-1]
                stack.pop()
            stack.append(key)
        return res_list


def test():
    t = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(t))


if __name__ == '__main__':
    test()