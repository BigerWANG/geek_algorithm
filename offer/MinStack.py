# coding: utf-8

"""
包含min函数的栈
"""

u"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.

"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self.__min = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._stack.append(x)
        if not self.__min or x <= self.__min[-1]:
            self.__min.append(x)

    def pop(self):
        """
        :rtype: None
        """
        pop_data = None
        if self._stack:
            pop_data = self._stack.pop()
            if pop_data == self.__min[-1]:
                self.__min.pop()
        return pop_data

    def top(self):
        """
        :rtype: int
        """
        if self._stack:
            return self._stack[-1]
        return None

    def min(self):
        """
        :rtype: int
        """
        return self.__min[-1]


s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)
print s.top()
print s.pop()

print s.min()
