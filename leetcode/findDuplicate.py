# coding: utf-8

"""
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思路：
        从前往后取每一个数，在剩下的数组中使用二分查找查询这个数
        需要对剩余数组排序
        时间复杂度O(n*logn)
        """
        if not nums:
            return -1
        nums.sort()
        # 从头开始查找
        for i in range(len(nums)):
            target = nums[i]
            _nums = nums[i+1: ]
            if self.binary_search(_nums, target):
                return target
        return -1


    def binary_search(self, nums, target):
        start = 0
        end = len(nums)
        while start < end:
            mid = (start + (end-start)) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
        return False



if __name__ == '__main__':
    numbers = [1,3,4,2,2]
    print(Solution().findDuplicate(numbers))





