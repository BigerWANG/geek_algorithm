# coding: utf-8

"""
滑动窗口的最大值
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

"""
from collections import deque


class Solution(object):
    @staticmethod
    def maxSlidingWindow(nums, k):
        """
        暴力循环法
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or not k:
            return []
        start = 0
        end = start + k
        l = []
        while len(nums) + 1 > end:
            w = nums[start:end]
            l.append(max(w))  # 每次取窗口内的最大值放到列表中
            start += 1
            end = start + k
        return l

    def maxSlidingWindow1(self, nums, k):
        """
        双端队列法
        1， 每次将窗口放到队列中，比较队列中的大小
        2，选出来最大的值放到队列最左边，其他的小于最大值的出队
        3，新进来的元素与最大值比较如果小于则忽略，如果大于则替换掉
        :param nums:
        :param k:
        :return:
        """
        if not nums or not k:
            return []
        start = 0
        end = start + k
        l = []
        while len(nums) + 1 > end:
            w = nums[start:end]
            l.append(self.append_deque(w))
            start += 1
            end = start + k
        return l

    def append_deque(self, w):
        """接收滑动窗口的并返回最大值"""
        d = deque()
        if not w:
            return None
        for i in w:
            if d:
                if d[0] > i:
                    continue
                else:
                    d.pop()
            d.appendleft(i)
        return d[0]

    def maxSlidingWindow2(self, nums, k):
        """
        构建大顶堆
        1， 每次将窗口放到队列中，比较队列中的大小
        2，选出来最大的值放到队列最左边，其他的小于最大值的出队
        3，新进来的元素与最大值比较如果小于则忽略，如果大于则替换掉
        :param nums:
        :param k:
        :return:
        """












def test():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(Solution().maxSlidingWindow2(nums, k))





if __name__ == '__main__':
    test()
