# coding: utf-8




class MyCircularQueue(object):
    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k + 1  # 队列长度, 循环队列需要多一个存储空间保存tail
        self.head, self.tail = 0, 0
        self.queue = [0] * self.k

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
        if self.isEmpty():
            return False
        # self.queue[self.head] = None
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