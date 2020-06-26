# coding: utf-8

"""
队列的最大值
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是

"""


class MaxQueue(object):
    """
    维护一个递减队列
    从队列尾部插入元素时，可以提前取出队列中所有比这个元素小的元素，
    这样的方法等价于要求维护队列单调递减，即要保证每个元素前边都没有比它小的元素，
    """

    def __init__(self):
        self.q = []
        self._max_values = []  # 这是一个递减队列，即每个元素前边都没有比它小的元素

    def max_value(self):
        """
        :rtype: int
        """
        if not self.q:
            return -1
        return self._max_values[0] if self._max_values else None

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        # 判断max_value的最后一个值如果小于value就pop掉
        # 这一步是维护一个递减队列
        while self._max_values and self._max_values[-1] < value:
            self._max_values.pop()
        self._max_values.append(value)
        self.q.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if not self.q:
            return -1
        p_data = self.q.pop(0)
        if self._max_values and p_data == self._max_values[0]:
            self._max_values.pop(0)
        return p_data



def test():
    pass




if __name__ == '__main__':
    test()
