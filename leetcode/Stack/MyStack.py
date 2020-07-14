# coding: utf-8

"""
用队列实现一个栈
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空

"""

from collections import deque

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()  # 初始化一个队列

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        size = len(self.q)
        self.q.append(x)
        for _ in range(size):  
            # 把队列从前往后加进来， 把头加到尾就行了
            self.q.append(self.q.popleft())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q[0] 

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
