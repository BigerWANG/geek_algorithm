# coding: utf-8

"""
基于数据实现一个队列
"""

from array import array


class ArrayQueue(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None for _ in range(capacity)]  # 定义一个定长的数组
        self.head = 0
        self.tail = 0

    def _enqueue(self, item):
        """
        入队操作
        无数据搬移
        :param item:
        :return:
        """

    def enqueue(self, item):
        """
        入队操作
        :param item:
        :return:
        """
        if self.tail == self.capacity:  # tail == capacity表示队列末尾没有位置了
            if self.head == 0:
                # 表示数据已经满了, head之前也没有空间
                return False
            # 开始数据搬移
            i = self.head
            print self.head
            print self.tail
            while self.head < self.tail:
                print self.items[i-self.head]
                print ">>i", i
                print self.items[i]
                self.items[i-self.head] = self.items[i]
                i += 1
            self.tail -= self.head
            self.head = 0

        self.items[self.tail] = item
        self.tail += 1
        print self.items
        return True

    def dequeue(self):
        """
        出队操作
        :return:
        """
        if self.head == self.tail:
            return None
        ret = self.items[self.head]
        self.items[self.head] = None
        self.head += 1
        print ">>deque>>", self.items
        return ret


def test():
    a = ArrayQueue(10)

    a.enqueue("a")
    a.enqueue("b")
    a.enqueue("c")

    print a.dequeue()
    print a.dequeue()
    a.enqueue("d")
    a.enqueue("e")
    a.enqueue("f")
    a.enqueue("g")
    a.enqueue("h")
    a.enqueue("i")
    a.enqueue("j")
    a.enqueue("k")
    a.enqueue("h")

if __name__ == '__main__':
    test()

