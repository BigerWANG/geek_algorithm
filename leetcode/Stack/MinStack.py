# coding: utf-8

"""
最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。

"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        使用一个辅助栈，top是最小值
        """
        self.stack = []
        self.min_stack = []  # 保存最小值

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.min_stack or x <= self.min_stack[-1]:  # 如果最小栈是空或者top <= x
            self.min_stack.append(x)
        self.stack.append(x)


    def pop(self):
        """
        :rtype: None
        """
        d = self.stack.pop()
        if d == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        return None


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1] if self.min_stack else None

def test():
	m = MinStack()
	m.push(0)
	m.push(1)
	m.push(0)
	print m.getMin()
	print m.pop()
	print m.getMin()

if __name__ == '__main__':
	test()




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()