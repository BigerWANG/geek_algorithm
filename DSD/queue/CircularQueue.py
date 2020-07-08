# coding: utf-8

"""
循环队列， 解决数据搬移的问题
"""





class CircularQueue(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None for _ in range(capacity)]
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        """
        入队操作
        :param item:
        :return:
        """
        if self.tail == self.capacity:
            return False
        self.items[self.tail] = item
        self.tail += 1

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
        return ret


def test():
    pass




if __name__ == '__main__':
    test()

