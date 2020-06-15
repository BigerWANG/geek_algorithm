# coding: utf-8

"""

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

"""
思路1：
优先级队列，使用大顶堆
每次维护heap，返回堆顶元素

思路2：
使用双端队列，前K个元素依次加入队列



"""


class Solution(object):

    def max_sliding_window0(self, nums, k):
        """
        双端队列法
        :type nums: List[int] 队列
        :type k: int 下标
        :rtype: List[int]
        """
        if not nums:
            return []
        window, res = [], []
        # 依次把数组中的元素放到window中，并且计算出最大值
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i-k:  # 判断
                window.pop(0)
            while window and nums[window[-1]] <= x:  # 如果新进入的元素比window中的最大元素大，那么就把window的所有小于X的元素都pop掉
                window.pop()
            window.append(i)  # 最后把最大值放入window中
            if i > k - 1:
                res.append(nums[window[0]])
        return res

    def max_sliding_window1(self, nums, k):
        """
        使用大顶堆
        时间复杂度O(NlogK)
        :type nums: List[int] 队列
        :type k: int 下标
        :rtype: List[int]
        """
        if not nums:
            return []
