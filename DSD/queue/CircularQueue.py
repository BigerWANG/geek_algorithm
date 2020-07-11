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


class CircularQueue(object):
    def __init__(self, capacity):
        self.capacity = capacity + 1
        self.items = [None for _ in range(capacity + 1)]
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        """
        入队操作
        :param item:
        :return:
        """
        if (self.tail + 1) % self.capacity == self.head:
            return False
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
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
        self.head = (self.head + 1) % self.capacity
        return ret

    def print_queue(self):
        print self.items
        print "head:", self.items[self.head], "index:", self.head
        print "tail:", self.items[self.tail], "index:", self.tail


def test():
    a = CircularQueue(3)

    a.enqueue("a")
    a.enqueue("b")
    a.enqueue("c")


    a.print_queue()




if __name__ == '__main__':
    test()

