# coding: utf-8

"""
搜索旋转排序数组

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        方法1：
        将数组分成[l, mid], [mid + 1, r]
        比较所在target在哪个区间，并且判断这个区间是否有序

        方法二：
        将数组分成两个有序的区间，找到最小值，分开
        看tagret属于哪个区间，就在哪个区间里找
        相当于两个二分法
        """

        if not nums:
            return -1
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid

            # 判断有序的方法： start <  end
            # 这里判断如果左半段有序

            if nums[mid] >= nums[start]:
                # 如果target在左半段
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            else:  # 如果是右半段有序
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


s = Solution()
a = \
[4,5,6,7,0,1,2]

print s.search(a, 0)









