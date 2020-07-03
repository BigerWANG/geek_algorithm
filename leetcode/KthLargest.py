# coding: utf-8

import heapq

"""
实时判断数据流中第K大元素
"""

"""
1，保存前K个最大值，每次排序取出最大元素 时间复杂度N* KlogK
2，优先级队列，维护一个小顶堆，堆的大小为K，每次取出堆顶元素
"""


class KthLargest:
    def __init__(self, k, nums):
        """

        """
        self.pool = nums
        self.size = len(self.pool)
        self.k = k
        # heapq.heapify 将列表原地转换为堆并只保留K个大小
        heapq.heapify(self.pool)
        while self.size > k:
            heapq.heappop(self.pool)
            self.size -= 1

    def add(self, val):
        """
        :param val:
        :return:
        """
        if self.size < self.k:  # 如果堆的长度小于K，val入堆
            heapq.heappush(self.pool, val)
            print self.pool
        elif val > self.pool[0]:  # 如果val大于堆顶元素，去掉堆顶重新入堆，并且堆化
            heapq.heapreplace(self.pool, val)
            print self.pool

        return self.pool[0]


if __name__ == '__main__':
    import random
    l = range(10)
    random.shuffle(l)
    print l
    print KthLargest(9, l).add(100)

