# coding: utf-8

"""
153. 寻找旋转排序数组中的最小值

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        找到变化点：
        所有变化点的左侧元素 > 起始点
        所有变化点的右侧元素 < 起始点

        算法：
        当中间值 > 最后一个元素：说明中间值左边的所有元素都大于后最一个元素，所以砍掉中间值前的所有元素，start = mid + 1
        当中间值 < 最后一个元素：说明中间值的左边的所有元素都小于后最一个元素，所以砍掉中间值后边的所有元素 end = mid

        这样不停的缩小区间，最后会缩小到1个节点，循环结束
        返回这个节点就可以了

        """

        if not nums:
            return -1

        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        # print end
        # print mid
        # print start

        return nums[end]



a = [2,1]


s = Solution().findMin(a)
