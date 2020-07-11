# coding: utf-8

"""
数据流中的移动平均值


给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算其所有整数的移动平均值。


MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

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
    print a.next(1)
    print a.next(10)
    print a.next(3)
    print a.next(5)


if __name__ == '__main__':
    test()