# coding: utf-8

"""
队列的最大值
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是

"""


class MaxQueue(object):

    def __init__(self):
        self.q = []

    def max_value(self):
        """
        :rtype: int
        """
        if not self.q:
            return -1


    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.q.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if not self.q:
            return -1
        return self.q.pop(0)


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()









def test():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(Solution().maxSlidingWindow2(nums, k))





if __name__ == '__main__':
    test()
