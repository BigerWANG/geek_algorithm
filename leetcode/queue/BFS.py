# coding: utf-8

"""
广度优先遍历 查询最短路径

"""


class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = list()

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue) >= self.size:
            self.queue.pop(0)
        self.queue.append(val)
        return float(sum(self.queue)) / len(self.queue)


def test():
    a = MovingAverage(3)
    print(a.next(1))
    print(a.next(10))
    print(a.next(3))
    print(a.next(5))


if __name__ == '__main__':
    test()