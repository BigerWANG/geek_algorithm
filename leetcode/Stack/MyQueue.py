# coding: utf-8


"""
用栈实现队列

做法：
定义两个栈 一个push，一个delete
push栈只接受入栈的操作，delete栈负责出栈的操作

出栈的时候把push pop到delete中

"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = []
        self.delete_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.push_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.delete_stack:  # 如果delete栈为空就把push的结果都pop到delete中
            while self.push_stack:
                self.delete_stack.append(self.push_stack.pop())
        return self.delete_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.delete_stack:
            while self.push_stack:
                self.delete_stack.append(self.push_stack.pop())
        return self.delete_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.push_stack and not self.delete_stack:
            return True
        return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()