# coding: utf-8

"""
34. 在排序数组中查找元素的第一个和最后一个位置

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.first(nums, target), self.last(nums, target)]

    def first(self, nums, target):
        """查询第一个匹配的数"""
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                # 判断mid 是不是第一个元素 或者 mid 的上一个节点不等于target
                if mid == 0 or nums[mid - 1] != nums[mid]:
                    return mid
                else:  # 如果不符合 说明找到了不是第一个targe的值
                    end = mid - 1
        return -1

    def last(self, nums, target):
        """查询最后一个匹配的数"""
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                # 判断mid 是不是最后一个元素 或者 mid 的下一个节点不等于target
                if mid == len(nums) - 1 or nums[mid + 1] != nums[mid]:
                    return mid
                else:  # 如果不符合 说明找到了不是最后一个targe的值
                    start = mid + 1
        return -1




s = Solution()
nums = [1]
target = 1
res = s.searchRange(nums, target)
print(res)
