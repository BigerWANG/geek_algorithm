# coding: utf-8

"""
循环队列， 解决数据搬移的问题
tail = 尾指针
head = 头指针
n = 队列长度

队列已满的判断条件：
(tail + 1) % n = head

每次入队尾指针后移一位
tail = (tail + 1) %n

每次出队，头指针后移一位
head = (head + 1) % n
"""


class MyCircularQueue(object):
    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k + 1  # 队列长度, 循环队列需要多一个存储空间保存tail
        self.head, self.tail = 0, 0
        self.queue = [0] * self.k

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
        return self.queue[(self.tail - 1) % self.k]

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