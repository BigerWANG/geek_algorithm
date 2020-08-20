# coding: utf-8

"""
设计你的循环队列实现

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。

"""


class MyCircularQueue(object):
    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k + 1  # 队列长度
        self.head, self.tail = 0, 0
        self.queue = [None for _ in range(self.k)]

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isFull():
            return False
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.k
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.head == self.tail

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return (self.tail + 1) % self.k == self.head


def test():
    a = MyCircularQueue(3)
    print(a.enQueue(1))
    print(a.enQueue(2))
    print(a.enQueue(3))
    print(a.enQueue(4))







if __name__ == '__main__':
    test()
